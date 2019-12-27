FROM python:3.7-alpine

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD requirements.txt /
RUN pip3 install -r requirements.txt

# copy project
RUN mkdir api
COPY ./account /api

# set work directory
WORKDIR /api/

RUN python3 manage.py migrate

EXPOSE 8080
