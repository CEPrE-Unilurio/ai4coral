FROM arm32v8/python

ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

COPY . .
CMD [ "make", "run" ]