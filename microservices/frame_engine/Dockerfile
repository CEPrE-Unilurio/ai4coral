FROM arm32v7/python:3.7.5-slim

WORKDIR /usr/src/app

ENV VIRTUAL_ENV "/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .

RUN apt update
RUN apt dist-upgrade
RUN apt clean

#RUN apt install libgl1-mesa-glx
RUN pip install --upgrade pip

RUN pip install --upgrade pip setuptools
RUN pip install --upgrade pip setuptools wheel

RUN pip3 install numpy==1.19.0

RUN apt-get install -y libhdf5-dev libc-ares-dev libeigen3-dev gcc gfortran python-dev libgfortran5 libatlas3-base libatlas-base-dev libopenblas-dev libopenblas-base libblas-dev liblapack-dev cython libatlas-base-dev openmpi-bin libopenmpi-dev python3-dev

# RUN python -m pip install --no-binary -r cmake

# RUN pip install -r requirements.txt

# RUN python -m pip install requests

# RUN python -m pip install opencv-python
# RUN python -m pip install numpy
RUN python -m pip install opencv-python-headless

COPY youcv.py .
CMD [ "python", "youcv.py" ] 
