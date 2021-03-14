# Copyright 2021  CEPrE-Unilurio 


r""" Control the services that coordinate to do object detections
 Usage:
  python servicectl.py [command] --service [name_of_the service]

  ex.:
    to run the api do:
      python service_ctl run --service ai4coral_api
"""

from od import ai4coral_api
from fe.frame_stream import VideoStream
from fe.settings import common as fe_config
from od.settings import common as od_config

import os
from absl import app
from absl import flags

services = ['ai4coral_api', 'frame_engine']
commands = ['run', 'stop', 'restart']

flags.DEFINE_string('service', None, 'The name of the service to run')

FLAGS = flags.FLAGS

def main(argv):
  command = argv[1]

  if command not in commands:
    raise ValueError(f'Only the following commands are available {commands}')
  
  if FLAGS.service not in services or FLAGS.service is None:
    raise ValueError(f'Only the following services are available {services}')
  
  if command == 'run':
    if FLAGS.service == 'ai4coral_api':
      print(f'OD_DIR {od_config.OD_DIR}, PID {os.getpid()}')
      ai4coral_api.run()
    elif FLAGS.service == 'frame_engine':
      VideoStream(src = str(fe_config.DATA_TEST_DIR) + '/test_video.mp4')
    

if __name__ == '__main__':
  app.run(main)