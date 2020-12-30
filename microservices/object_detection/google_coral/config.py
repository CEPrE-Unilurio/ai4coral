from detector_base import load_labels

# input shape
W = 640
H = 640
C = 3

SAMPLE_XML_ANNOTATION_PATH = "annotation.xml"
FOLDER_NAME = "ai4coral2021"
PATH_TO_LABELS = 'models/coco_labels.txt'
LABELS = load_labels(PATH_TO_LABELS)
PATH_TO_MODEL = 'models/ssd_mobilenet_v2_coco_quant_postprocess.tflite'
THRESHOLD = 0.4