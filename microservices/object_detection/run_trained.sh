python3 detector_base.py \
--model models/core.tflite \
--labels models/demo_labels.txt \
--input images/starfish.jpg \
--output images/starfish_processed.jpg \
--threshold 0.1 \
--count 1
