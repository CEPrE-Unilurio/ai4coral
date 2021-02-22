from .development import *
from os.path import join 

PATH_TO_MODEL = join(OD_DIR, 'models/ssd_mobilenet_v2_coco_quant_postprocess_edgetpu.tflite')
PATH_TO_LABELS = join(OD_DIR, 'models/coco_labels.txt')