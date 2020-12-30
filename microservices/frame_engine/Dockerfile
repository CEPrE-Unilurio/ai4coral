
FROM continuumio/miniconda

WORKDIR /opt

# RUN conda create -n tf tensorflow

SHELL ["conda", "run", "-n", "tf", "/bin/bash", "-c"]

RUN apt-get update &&  apt-get install build-essential -y
RUN python -m pip install opencv-python
RUN python -m pip install camera
RUN apt-get install python-picamera python3-picamera
RUN python -m pip install requests

COPY . .

ENTRYPOINT ["conda", "run", "-n", "tf", "make", "run"]
