.PHONY = help run clean run_demo_pretrained run_demo_trained

run:
	gunicorn -w 12 detector:app --bind 0.0.0.0:8080

run_demo_pretrained:
	@bash run_pretrained.sh

run_demo_trained:
	@bash run_trained.sh

help:
	@echo "----------------------- Help -----------------------"
	@echo "make run_container - use this to run the api inside a docker  container"
	@echo "make setup - use this to build the docker image"
