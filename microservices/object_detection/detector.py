from config import PATH_TO_MODEL, THRESHOLD
import detector_base
from logger import logger
import detect
from annotator import Annotator
from timing import timeit, to_string
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

  
@route('/')
def greetings():
  return "Hi, I am the AI4Coral RESTful API\n"

@post('/detect/<filename>')
def do_detections(filename):
  try:
    logtime_data = {}

    data = request.body
    image = detector_base.load_image(data, log_time=logtime_data)
    
    interpreter = detector_base.make_interpreter(PATH_TO_MODEL,
                                                log_time=logtime_data)
    
    scale = detect.set_input(interpreter, image.size,
                           lambda size: image.resize(size, Image.ANTIALIAS),
                           log_time=logtime_data)
    
    detector_base.invoke_interpreter(interpreter,
                                      log_time=logtime_data)

    objs = detect.get_output(interpreter, THRESHOLD, scale,
                            log_time=logtime_data)
    
    ann = Annotator()
    annotations = ann.get_annotations(objs=objs, filename=filename, 
                                      log_time=logtime_data)
    performance_log.info(to_string(logtime_data))
    return annotations
  except Exception as e:
    response.status = 400
    error_plus_log.exception("detection failed")
    return "detection failed"
        
if __name__ == '__main__':
     run(host='localhost', port=8080)

app = bottle.default_app()
