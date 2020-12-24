.PHONY = help setup test run clean


setup:
	@echo "building docker image named ai4coral"
	docker build -t ai4coral .
run:
	gunicorn -w 12 detector:app --bind 0.0.0.0:8000
clean:
	docker image prune
	docker container prune
