# ai4coral

# Description
This project is meant to be deployed in Raspberry for underwater data collect.

# Overview
The ai4coral is based on client-server arquitecture
![Alt text](ai4coral_overview.png?raw=true "Title")

# How to Run the project

# 1 - Install python create virtaulenv and install packages: 

    $ make deploy=[true|false] setup
    true - when setting up production environment
    false - when setting up development environment 

# 2 - Start Server
    $ make run_api 

# 3 - Start Frame_Engine
    $ make run_frame_engine
    
# 4 - Project Structure
``` bash
ai4coral/
├── ai4coral_overview.png
├── api_timing_report.ipynb
├── Coral_Data
├── deploy.sh
├── gunicorn.bash
├── LICENSE
├── log
│   ├── api_error.log
│   ├── api_timing.csv
│   ├── api_timing_header.csv
│   └── api_warning.log
├── Makefile
├── microservices
│   ├── Coral_Data
│   ├── frame_engine
│   │   ├── cameraCV.py
│   │   ├── config.py
│   │   ├── frame_stream.py
│   │   ├── __init__.py
│   │   └── thread_request.py
│   └── object_detection
│       ├── annotator.py
│       ├── api.raml
│       ├── core
│       │   └── __init__.py
│       ├── detector_base.py
│       ├── detector.py
│       ├── detect.py
│       ├── howto
│       ├── __init__.py
│       ├── logger.py
│       ├── models
│       │   ├── coco_labels.txt
│       │   ├── core.tflite
│       │   ├── demo_labels.txt
│       │   ├── ssd_mobilenet_v2_coco_quant_postprocess_edgetpu.tflite
│       │   └── ssd_mobilenet_v2_coco_quant_postprocess.tflite
│       ├── README.md
│       ├── run_pretrained.sh
│       ├── run_trained.sh
│       ├── settings
│       │   ├── common.py
│       │   ├── development.py
│       │   ├── __init__.py
│       │   ├── production.py
│       ├── tests
│       │   ├── images
│       │   │   ├── fish_processed.jpg
│       │   │   ├── grace_hopper.bmp
│       │   │   ├── grace_hopper_processed.bmp
│       │   │   ├── image1.jpg
│       │   │   ├── image1_processed.jpg
│       │   │   ├── image2.jpg
│       │   │   ├── starfish.jpg
│       │   │   ├── starfish_processed.jpg
│       │   │   └── test_video.mp4
│       │   ├── stress_api.py
│       │   └── stress_test.sh
│       ├── tests.py
│       ├── timing.py
│       └── utils
│           └── __init__.py
├── README.md
├── requirements.txt
├── run_frame_engine.bash
├── scripts
│   └── stress_api.sh
└── setup.bash
```
