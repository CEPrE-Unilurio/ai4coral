# input shape
INPUT_SHAPE = (640, 640, 3)
DEBUG = True
FOLDER_NAME = "ai4coral2021"
PATH_TO_LABELS = 'models/coco_labels.txt'

PATH_TO_MODEL = None

if DEBUG:
  PATH_TO_MODEL = 'models/ssd_mobilenet_v2_coco_quant_postprocess.tflite'
else:
  PATH_TO_MODEL = 'models/ssd_mobilenet_v2_coco_quant_postprocess_edgetpu.tflite'

THRESHOLD = 0.4