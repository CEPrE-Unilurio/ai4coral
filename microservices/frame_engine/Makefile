.PHONY = help setup test run clean

setup: Dockerfile
	@echo "building docker image named frameEngine"
	docker build -t frameEngine .
run:
	 docker run -p 8080:8080 frameEngine
clean:
	docker image prune
	docker container prune
help:
	@echo "----------------------- Help -----------------------"
	@echo "make run_container - use this to run the api inside a docker  container"
	@echo "make setup - use this to build the docker image"
