OD_DIR=microservices/object_detection

setup:
	@bash setup.bash $(deploy)
run_api:
	@bash gunicorn.bash
run_frame_engine:
	@bash run_frame_engine.bash
test_object_detection:
	$(shell cd $(OD_DIR); python tests.py)
