FROM python:3.7-alpine

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# preinstall some requirements so we don't
# reinstall them everytime requirements.txt changes
RUN pip3 install Django==3.0.1
RUN pip3 install djangorestframework==3.11.0
RUN pip3 install gunicorn==20.0.4
RUN pip3 install whitenoise==5.0.1

# unfortunatly python alpine needs those packages
# in order to install postgres support
RUN apk --no-cache add build-base
RUN apk --no-cache add postgresql-dev
RUN pip3 install psycopg2

ADD requirements.txt /
RUN pip3 install -r requirements.txt

# copy project
RUN mkdir api
COPY ./ /api

# set work directory
WORKDIR /api/

RUN python3 manage.py collectstatic --noinput

EXPOSE 8080
