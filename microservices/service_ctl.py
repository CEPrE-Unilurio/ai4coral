# Copyright 2021  CEPrE-Unilurio 

r""" Control the services that coordinate to do object detections
 Usage:
  python servicectl.py [command] --service [name_of_the service]

  ex.:
    to start the api do:
      python service_ctl start --service ai4coral_api

    to stop (kill) the api do:
      python service_ctl stop --service ai4coral_api

    to restart  the api do:
      python service_ctl restart --service ai4coral_api
  
  COLUMNS for scheduler log file
    MSG, SERVICE_NAME, TIME_STAMP       

"""

from od import ai4coral_api
from fe.frame_stream import VideoStream
from fe.settings import common as fe_config
from od.settings import common as od_config
import os, signal
from absl import app
from absl import flags
from od.utils.logger import logger

scheduler_log = logger(name=od_config.SCHEDULER_LOG['name'], filename=od_config.SCHEDULER_LOG['filename'], 
                  fmt='%(asctime)s, %(message)s')

error_log = logger(name=od_config.ERROR_LOG['name'], filename=od_config.ERROR_LOG['filename'])

services = ['ai4coral_api', 'frame_engine']
commands = ['start', 'stop', 'restart']
PID = str(os.getpid())
flags.DEFINE_string('service', None, 'The name of the service to start | stop | restart')
FLAGS = flags.FLAGS


def log(msg, service_name):
  scheduler_log.info(f'{msg}, {service_name}')

def main(argv):
  command = argv[1]
  if command not in commands:
    raise ValueError(f'Only the following commands are available {commands}')
  if FLAGS.service not in services or FLAGS.service is None:
    raise ValueError(f'Only the following services are available {services}')
  
  def start():
    if FLAGS.service == 'ai4coral_api':
      os.system('fuser -k 8080/tcp')
      log('STARTING', FLAGS.service)
      ai4coral_api.run()
    elif FLAGS.service == 'frame_engine':
      with open(f'{fe_config.FE_DIR}/{FLAGS.service}.pid','w') as fe_pidfile:
        fe_pidfile.write(PID)
      with open(f'{fe_config.FE_DIR}/{FLAGS.service}.pid','r') as fe_pidfile:
        if fe_pidfile.readlines()[0].strip() == PID:
          log('STARTING', FLAGS.service)
          VideoStream(src = str(fe_config.DATA_TEST_DIR) + '/test_video.mp4',
                        show_frame=False)

  def stop():
    if FLAGS.service == 'ai4coral_api':
      log('STOPING', FLAGS.service)
      os.system('fuser -k 8080/tcp')  
    elif FLAGS.service == 'frame_engine':
      with open(f'{fe_config.FE_DIR}/{FLAGS.service}.pid','r') as fe_pidfile:
        PID = int(fe_pidfile.readlines()[0].strip())
        log('STOPING', FLAGS.service)  
        os.kill(PID, signal.SIGKILL)
      os.system(f'rm {fe_config.FE_DIR}/{FLAGS.service}.pid')
  
  if command == 'start':
    try:
      start()
    except Exception as e:
      error_log.exception("error starting service")
  elif command == 'stop':
    try:
      stop()
    except Exception as e:
      error_log.exception("error stoping service")
if __name__ == '__main__':
  app.run(main)