import os
from pathlib import Path

# input shape
W = 640
H = 640
FPS = 24.0

img_format = '.png'
num_thread = 4

urlapi = 'http://localhost:8080/detect'

CORAL_DATA_DIR = Path(__file__).parent.parent / "../Coral_Data/"

if not os.path.exists(CORAL_DATA_DIR):
    os.makedirs(CORAL_DATA_DIR)

data_test_directory = Path(__file__).parent / "../object_detection/images/"
