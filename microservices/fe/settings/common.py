import os
from pathlib import Path

################# IMPUT SHAPE #############################
#DELAY_TIME is used to control de fps
#Example if DELAY_TIME = 200 then fps = 1000/200
DELAY_TIME = 200 
HIGH_VALUE = 100000
WIDTH = HIGH_VALUE
HEIGHT = HIGH_VALUE
FPS = 4.0
IMG_FORMAT = '.png'

####################### OTHER VARIABLE ####################
NUM_THREAD = 4

################ URL PATH TO API ##########################
URL_API = 'http://localhost:8080/detect'

################ PATH FOR STORED DATA ######################
CORAL_DATA_DIR = Path(__file__).parent.parent.parent / "../coral_data/"

if not os.path.exists(CORAL_DATA_DIR):
    os.makedirs(CORAL_DATA_DIR)

################### PATH FOR TEST DATA #####################
DATA_TEST_DIR = Path(__file__).parent.parent / "../od/tests/images/"
