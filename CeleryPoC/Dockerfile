FROM python:3.9.9

RUN pip install celery==5.2.1 pymongo==3.12.0 bottle
RUN adduser snyky

COPY *.py /
COPY views /views

EXPOSE 27017
