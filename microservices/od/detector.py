from od.settings.common import DEBUG  

if DEBUG:
  from od.settings import development as config
else:
  from od.settings import production as config

from od.core import detector_base
from od.core import detect
from od.utils.logger import logger
from od.utils.timing import to_string
import bottle
from bottle import route, run,  get, post, request, response
import io

from PIL import Image
from PIL import ImageDraw
import time

timing_log = logger(name=config.TIMING_LOG['name'], 
                    filename=config.TIMING_LOG['filename'], 
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
    interpreter = detector_base.make_interpreter(config.PATH_TO_MODEL, log_time=logtime_data)
    scale = detect.set_input(interpreter, image.size, image, log_time=logtime_data)
    

    detector_base.invoke_interpreter(interpreter, log_time=logtime_data)
    annotations = detect.get_output(interpreter, 
                                    config.THRESHOLD, 
                                    scale, 
                                    log_time=logtime_data,
                                    filename=filename)
    timing_log.info(to_string(logtime_data))
    return annotations
  except Exception as e:
    response.status = 400
    detector_base.error_log.exception("detection failed")
    return "detection failed"
        
if __name__ == '__main__':
     run(host='localhost', port=8080)

app = bottle.default_app()
