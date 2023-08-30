FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /dswa

ADD . /dswa

RUN pip install -r requirements.txt


