setup:
	@bash setup.bash $(deploy)
run_api: setup
	@bash gunicorn.bash

run_frame_engine:
	@bash run_frame_engine.bash
