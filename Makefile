setup:
	@bash setup.bash $(deploy)
run_api:
	@bash gunicorn.bash
run_frame_engine:
	@bash run_frame_engine.bash
test_object_detection:
	@bash cd microservices/object_detection
	@python tests.py
