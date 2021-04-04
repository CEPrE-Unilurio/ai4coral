#!/bin/bash
#
# Copyright 2021  CEPrE-Unilurio 

#default values 

OD_DIR=microservices/od
MS_DIR=microservices
#remenber to change this
#it needs improvement

deploy=false

setup:
	@bash scripts/setup.sh $(deploy)
setup_scheduler:
	python $(MS_DIR)/scheduler.py
start_api:
	python $(MS_DIR)/service_ctl.py start --service ai4coral_api
stop_api:
	python $(MS_DIR)/service_ctl.py stop --service ai4coral_api
start_frame_engine:
	python $(MS_DIR)/service_ctl.py start --service frame_engine
stop_frame_engine:
	python $(MS_DIR)/service_ctl.py stop --service frame_engine
unit_test_api:
	python $(OD_DIR)/tests/unit_tests.py
stress_api: 
	python $(OD_DIR)/tests/stress_api.py
cpu_monitor:
	@bash scripts/cpu_monitor.sh
	
