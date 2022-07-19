FROM python:alpine3.16

COPY . /home

WORKDIR /home

RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

CMD flask run --host=0.0.0.0
