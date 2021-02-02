OD_DIR=microservices/object_detection

setup:
	@bash scripts/setup.sh $(deploy)
run_api:
	@bash scripts/run_api.sh
run_frame_engine:
	@bash scripts/run_frame_engine.sh
unit_test_api:
	$(shell cd $(OD_DIR); python tests/unit_tests.py)
timing_api:
	$(shell cp -f log/api_timing_header.csv log/api_timing.csv) 	
	@bash run_frame_engine.sh
stress_api: 
	$(shell cp -f log/api_timing_header.csv log/api_timing.csv) 	
	@bash scripts/stress_api.sh
cpu_monitor:
	@bash scripts/cpu_monitor.sh
	
