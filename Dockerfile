FROM python:3.11

WORKDIR /home

ENV FLASK_APP=main.py


RUN apt-get update

COPY ./requirements.txt ./requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
