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

# 2 - export ai4coral packages to PYTHONPATH, etc
    $ source configure.sh

# 3 - Start Server
    $ make run_api 

# 4 - Start Frame_Engine
    $ make run_frame_engine
    
# 5 - Project Structure
``` bash
ai4coral/
├── coral_data
├── logs
├── microservices
│   ├── Coral_Data
│   ├── fe
│   └── od
│       ├── core
│       ├── demos
│       ├── docs
│       ├── models
│       ├── settings
│       ├── tests
│       └── utils
├── noteboks
├── resource
├── scripts
└── venv
```
