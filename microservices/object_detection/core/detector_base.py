# Lint as: python3
# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Example using TF Lite to detect objects in a given image."""

from settings.common import DEBUG  

if DEBUG:
  from settings import development as config
  import tensorflow.lite as tflite
else:
  from settings import production as config
  import tflite_runtime.interpreter as tflite
  
import argparse
import time

from PIL import Image
from PIL import ImageDraw

from core import detect
from utils.logger import logger
from utils.timing import timeit

error_log = logger(name=config.ERROR_LOG['name'], filename=config.ERROR_LOG['filename'])
warning_log = logger(name=config.WARNING_LOG['name'], filename=config.WARNING_LOG['filename'])

class TFLiteSingleton:   
  __instance = None
  __interpreter = None 
  __is_using_edgetpu = None
    
  def __init__(self):
    if TFLiteSingleton.__instance != None:
      raise NotImplemented("This is a singleton class.")
 
  @staticmethod
  def get_instance(model_file):        
    if TFLiteSingleton.__instance == None:
      try:
        TFLiteSingleton.interpreter = tflite.Interpreter(model_path=model_file,
          experimental_delegates=[tflite.load_delegate('libedgetpu.so.1')])
        TFLiteSingleton.is_using_edgetpu = True
        TFLiteSingleton.__instance = TFLiteSingleton()
        return TFLiteSingleton.__instance
      except Exception as e:
        TFLiteSingleton.interpreter  =  tflite.Interpreter(model_path=model_file)
        TFLiteSingleton.is_using_edgetpu = False
        TFLiteSingleton.__instance = TFLiteSingleton()
        warning_log.warning('Could not load dynamic library \'libedgetpu.so.1\' none ops will be delegated to coral edgetpu')
        return TFLiteSingleton.__instance
    else:
      return TFLiteSingleton.__instance

  @property
  def is_using_edgetpu(self):
    return self.__is_using_edgetpu

  @is_using_edgetpu.setter
  def is_using_edgetpu(self, value):
    self.__is_using_edgetpu = value

  @property
  def interpreter(self):
    return self.__interpreter

  @interpreter.setter
  def interpreter(self, value):
    self.__interpreter = value

  def info(self):
    interpreter = self.interpreter
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    print("--------------------------------------------- inputs details -----------------------------")
    print(input_details)
    print("--------------------------------------------- output details -----------------------------")
    print(output_details)

@timeit
def load_image(data, **kwargs):
  """Load an image from raw bytes.

  Args:
    data: byte streams
  Returns:
    an image object
  """

  return Image.open(data)
  
@timeit
def invoke_interpreter(interpreter, **kwargs):
  interpreter.invoke()

@timeit
def make_interpreter(model_file, **kwargs):
  tfls = TFLiteSingleton.get_instance(model_file=model_file)
  tfls.interpreter.allocate_tensors()
  return tfls.interpreter 
    

def draw_objects(draw, objs, labels):
  """Draws the bounding box and label for each object."""
  for obj in objs:
    bbox = obj.bbox
    draw.rectangle([(bbox.xmin, bbox.ymin), (bbox.xmax, bbox.ymax)],
                   outline='red')
    draw.text((bbox.xmin + 10, bbox.ymin + 10),
              '%s\n%.2f' % (labels.get(obj.id, obj.id), obj.score),
              fill='red')


def main():
  parser = argparse.ArgumentParser(
      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument('-m', '--model', required=True,
                      help='File path of .tflite file.')
  parser.add_argument('-i', '--input', required=True,
                      help='File path of image to process.')
  parser.add_argument('-l', '--labels',
                      help='File path of labels file.')
  parser.add_argument('-t', '--threshold', type=float, default=0.4,
                      help='Score threshold for detected objects.')
  parser.add_argument('-o', '--output',
                      help='File path for the result image with annotations')
  parser.add_argument('-c', '--count', type=int, default=5,
                      help='Number of times to run inference')
  args = parser.parse_args()

  labels = load_labels(args.labels) if args.labels else {}
  interpreter = make_interpreter(args.model)
  interpreter.allocate_tensors()

  image = Image.open(args.input)
  scale = detect.set_input(interpreter, image.size,
                           lambda size: image.resize(size, Image.ANTIALIAS))

  print('----INFERENCE TIME----')
  print('Note: The first inference is slow because it includes',
        'loading the model into Edge TPU memory.')
  for _ in range(args.count):
    start = time.perf_counter()
    interpreter.invoke()
    inference_time = time.perf_counter() - start
    objs = detect.get_output(interpreter, args.threshold, scale)
    print('%.2f ms' % (inference_time * 1000))

  print('-------RESULTS--------')
  if not objs:
    print('No objects detected')

  for obj in objs:
    print(labels.get(obj.id, obj.id))
    print('  id:    ', obj.id)
    print('  score: ', obj.score)
    print('  bbox:  ', obj.bbox)

  if args.output:
    image = image.convert('RGB')
    draw_objects(ImageDraw.Draw(image), objs, labels)
    image.save(args.output)
    image.show()


if __name__ == '__main__':
  main()
