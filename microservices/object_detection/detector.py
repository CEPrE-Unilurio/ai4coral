from config import PATH_TO_MODEL, THRESHOLD
import detector_base
from logger import logger
import detect
from annotator import Annotator
import bottle
from bottle import route, run,  get, post, request, response
import io
from PIL import Image
from PIL import ImageDraw
import time

error_plus_log = logger(name='error_plus_monitor',filename='api_error_plus.log')

performance_log = logger(name='api_performance_monitor',
                                  filename='api_perfomance.log', 
                                  fmt='%(message)s')


# need improvement
performance_log.info('load_tflite_t,load_image_t,preprocess_image_t,invoke_tensors_t,detect_t,annotate_t')
  
@route('/')
def greetings():
  return "Hi, I am the AI4Coral RESTful API\n"

@post('/detect/<filename>')
def do_detections(filename):
  try:
    start = time.perf_counter()
    interpreter = detector_base.make_interpreter(PATH_TO_MODEL)
    interpreter.allocate_tensors()
    load_tflite_t = 1000 * (time.perf_counter() - start)
    
    start = time.perf_counter()
    image_data = request.body
    image = Image.open(image_data)
    load_image_t = 1000 * (time.perf_counter() - start)
    
    start = time.perf_counter()
    scale = detect.set_input(interpreter, image.size,
                           lambda size: image.resize(size, Image.ANTIALIAS))
    preprocess_image_t = 1000 * (time.perf_counter() - start)
    
    start = time.perf_counter()
    interpreter.invoke()
    invoke_tensors_t = 1000 * (time.perf_counter() - start)
    
    start = time.perf_counter()
    objs = detect.get_output(interpreter, THRESHOLD, scale)
    detect_t = 1000 * (time.perf_counter() - start)

    start = time.perf_counter()
    ann = Annotator()
    annotations = ann.get_annotations(objs=objs, filename=filename)
    annotate_t = 1000 * (time.perf_counter() - start)

    performance_log.info(f'{load_tflite_t},{load_image_t},{preprocess_image_t},{invoke_tensors_t},{detect_t},{annotate_t}')
    return annotations
  except Exception as e:
    response.status = 400
    error_plus_log.exception("detection failed")
    return "detection failed"
        
if __name__ == '__main__':
     run(host='localhost', port=8080)

app = bottle.default_app()
