import logging
import sys


# input shape
INPUT_SHAPE = (640, 640, 3)

FOLDER_NAME = "ai4coral2021"
PATH_TO_LABELS = 'models/coco_labels.txt'
PATH_TO_MODEL = 'models/ssd_mobilenet_v2_coco_quant_postprocess.tflite'
THRESHOLD = 0.4


log = logging.getLogger()
log.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)

file_handler = logging.FileHandler('ai4coralapi.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)


log.addHandler(file_handler)
log.addHandler(stdout_handler)
