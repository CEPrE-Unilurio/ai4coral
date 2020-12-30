.PHONY = help setup test run clean


setup: Dockerfile
	@echo "building docker image named ai4coral"
	docker build -t ai4coral .
run:
	gunicorn -w 12 detector:app --bind 0.0.0.0:8080
run_container: setup
	 docker run -p 8080:8080 ai4coral
test:
	bash google_coral/run.sh
clean:
	docker image prune
	docker container prune
help:
	@echo "----------------------- Help -----------------------"
	@echo "make run_container - use this to run the api inside a docker  container"
	@echo "make setup - use this to build the docker image"
