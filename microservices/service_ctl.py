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
      
"""

from od import ai4coral_api
from fe.frame_stream import VideoStream
from fe.settings import common as fe_config
from od.settings import common as od_config

import os, signal
from absl import app
from absl import flags

services = ['ai4coral_api', 'frame_engine']
commands = ['start', 'stop', 'restart']
PID = str(os.getpid())
    
flags.DEFINE_string('service', None, 'The name of the service to run | stop | restart')

FLAGS = flags.FLAGS

def main(argv):
  command = argv[1]

  if command not in commands:
    raise ValueError(f'Only the following commands are available {commands}')
  
  if FLAGS.service not in services or FLAGS.service is None:
    raise ValueError(f'Only the following services are available {services}')
  
  def start():
    if FLAGS.service == 'ai4coral_api':
      with open(f'{od_config.OD_DIR}/pidfile','w') as od_pidfile:
        od_pidfile.write(PID)
      with open(f'{od_config.OD_DIR}/pidfile','r') as od_pidfile:
        if od_pidfile.readlines()[0].strip() == PID:
          print(f'starting {FLAGS.service} with PID {PID}')
          ai4coral_api.run()
    elif FLAGS.service == 'frame_engine':
      with open(f'{fe_config.FE_DIR}/pidfile','w') as fe_pidfile:
        fe_pidfile.write(PID)
      with open(f'{fe_config.FE_DIR}/pidfile','r') as fe_pidfile:
        if fe_pidfile.readlines()[0].strip() == PID:
          print(f'starting {FLAGS.service} with PID {PID}')
          VideoStream(src = str(fe_config.DATA_TEST_DIR) + '/test_video.mp4')

  def stop():
    if FLAGS.service == 'ai4coral_api':
      print(f'stoping {FLAGS.service}')
      with open(f'{od_config.OD_DIR}/pidfile','r') as od_pidfile:
        PID = int(od_pidfile.readlines()[0].strip())  
        os.kill(PID, signal.SIGKILL)
        print(f'{FLAGS.service} stoped')
    elif FLAGS.service == 'frame_engine':
      print(f'stoping {FLAGS.service}')
      with open(f'{fe_config.FE_DIR}/pidfile','r') as fe_pidfile:
        PID = int(fe_pidfile.readlines()[0].strip())  
        os.kill(PID, signal.SIGKILL)
        print(f'{FLAGS.service} stoped')
    
  if command == 'start':
    start()
  elif command == 'stop':
    stop()
    
if __name__ == '__main__':
  app.run(main)