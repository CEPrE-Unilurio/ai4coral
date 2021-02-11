cd ..

python3 core/detector_base.py \
--model models/core.tflite \
--labels models/demo_labels.txt \
--input tests/images/starfish.jpg \
--output tests/images/starfish_processed.jpg \
--threshold 0.1 \
--count 1