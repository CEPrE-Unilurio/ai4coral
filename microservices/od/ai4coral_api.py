
# Copyright 2021  CEPrE-Unilurio 

import multiprocessing

import gunicorn.app.base

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

@route('/hello')
def hello():
  return "hello"

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

def ai4coral_app():
  return bottle.default_app()

def number_of_workers():
  return (multiprocessing.cpu_count() * 2) + 1

class AI4CoralStandaloneApplication(gunicorn.app.base.BaseApplication):

  def __init__(self, app, options=None):
      self.options = options or {}
      self.application = app
      super().__init__()

  def load_config(self):
    config = {key: value for key, value in self.options.items()
                if key in self.cfg.settings and value is not None}
    for key, value in config.items():
      self.cfg.set(key.lower(), value)

  def load(self):
    return self.application

host = '0.0.0.0'
port = '8080'
options = {
  'name': 'AI4Coral API',
  'bind': f'{host}:{port}',
  'workers': number_of_workers(),
}

def run():
  AI4CoralStandaloneApplication(ai4coral_app(), options).run() 