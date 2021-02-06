#!/bin/bash
#
# Copyright 2021  CEPrE-Unilurio 

# export microservices packages to PYHTONPATH

cp ~/.bashrc ~/.bashrc.back
cp ~/.bashrc ~/.bashrc.back.back
rm ~/.bashrc 
python resource/python_path.py
source ~/.bashrc