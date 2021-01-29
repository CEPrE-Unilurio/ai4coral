OD_DIR=microservices/object_detection

setup:
	@bash setup.bash $(deploy)
run_api:
	@bash gunicorn.bash
run_frame_engine:
	@bash run_frame_engine.bash
test_object_detection:
	$(shell cd $(OD_DIR); python tests.py)
timing_api:
	$(shell cp -f log/api_timing_header.csv log/api_timing.csv) 	
	@bash run_frame_engine.bash
stress_api: 
	@bash stress_api.sh
	
