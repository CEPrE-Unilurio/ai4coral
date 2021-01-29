from os.path import abspath, basename, dirname, join, normpath
from pathlib import Path
import sys
import os

DEBUG = True # DEBUG = False when running in production

###### BASE PATH CONFIGURATION ################################

OD_DIR = dirname(dirname(abspath(__file__)))
AI4CORAL_DIR = dirname(dirname(OD_DIR))
API_NAME = basename(AI4CORAL_DIR)
LOG_DIR = join(AI4CORAL_DIR, 'log')
ERROR_LOG = {'filename': join(LOG_DIR, 'api_error.log'), 'name': 'api_error_logger'} 
WARNING_LOG = {'filename':join(LOG_DIR, 'api_warning.log'), 'name': 'api_warning_logger'} 
TIMING_LOG = {'filename': join(LOG_DIR, 'api_timing.csv'), 'name': 'api_timing_logger'} 

###### MODEL CONFIGURATION ################################

INPUT_SHAPE = (640, 640, 3)
FOLDER_NAME = "ai4coral2021"
PATH_TO_LABELS = join(OD_DIR, 'models/coco_labels.txt')
THRESHOLD = 0.4