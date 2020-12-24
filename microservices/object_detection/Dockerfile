FROM continuumio/miniconda

WORKDIR /opt

RUN conda create -n tf tensorflow

SHELL ["conda", "run", "-n", "tf", "/bin/bash", "-c"]

RUN apt-get update &&  apt-get install build-essential -y
RUN python -m pip install bottle
RUN  python -m pip install gunicorn

COPY . .

ENTRYPOINT ["conda", "run", "-n", "tf", "make", "run"]
