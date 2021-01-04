FROM python:3.7-stretch

# ENV VIRTUAL_ENV=/opt/venv
# RUN python -m venv $VIRTUAL_ENV
# ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# COPY requirements.txt .

RUN python -m pip install opencv-python
RUN python -m pip install requests


COPY . .
CMD [ "python", "cameraCV.py" ]
