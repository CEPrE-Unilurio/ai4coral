#!/bin/bash
#
# Copyright 2021  CEPrE-Unilurio 

#default values 

OD_DIR=microservices/od

#remenber to change this
#it needs improvement

deploy=false

setup:
	@bash scripts/setup.sh $(deploy)
run_api:
	@bash scripts/run_api.sh
run_frame_engine:
	@bash scripts/run_frame_engine.sh
unit_test_api:
	$(shell cd $(OD_DIR); python tests/unit_tests.py)
timing_api:
	$(shell cp -f logs/api_timing_header.csv log/api_timing.csv) 	
	@bash run_frame_engine.sh
stress_api: 
	$(shell cp -f logs/api_timing_header.csv logs/api_timing.csv) 	
	@bash scripts/stress_api.sh
cpu_monitor:
	@bash scripts/cpu_monitor.sh
	
