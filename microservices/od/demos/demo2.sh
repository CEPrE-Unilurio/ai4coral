cd ..
MODEL=models/ssd_mobilenet_v2_coco_quant_postprocess.tflite
LABELS=models/coco_labels.txt

python3 core/detector_base.py \
--model $MODEL \
--labels $LABELS \
--input tests/images/truck.png \
--output tests/images/truck_processed.png \
--threshold 0.5 \
--count 1