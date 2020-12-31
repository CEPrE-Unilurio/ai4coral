MODEL=models/ssd_mobilenet_v2_coco_quant_postprocess.tflite
LABELS=models/coco_labels.txt

python3 detector_base.py \
--model $MODEL \
--labels $LABELS \
--input images/image1.jpg \
--output images/image1_processed.jpg
