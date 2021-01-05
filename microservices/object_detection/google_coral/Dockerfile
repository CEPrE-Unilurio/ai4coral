FROM continuumio/miniconda

WORKDIR /opt

RUN conda create -n ai4coral tensorflow

SHELL ["conda", "run", "-n", "ai4coral", "/bin/bash", "-c"]

COPY . .
RUN pip install -r requirements.txt

ENTRYPOINT ["conda", "run", "-n", "ai4coral", "make", "run"]
