from pathlib import Path

# input shape
W = 640
H = 640
FPS = 1.0

urlapi = 'http://localhost:8080/detect'
BASE_DIR = Path('/')

data_test_directory = Path(__file__).parent / "../object_detection/google_coral/images/"