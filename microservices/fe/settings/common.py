import os
from pathlib import Path

################# IMPUT SHAPE #############################
WIDTH = 300
HEIGHT = 300
FPS = 24.0
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
