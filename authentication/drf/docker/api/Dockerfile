FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update && \
    apk upgrade && \
    apk add --no-cache mariadb-connector-c-dev mariadb-client && \
    apk add --no-cache --virtual .build-deps build-base mariadb-dev

RUN mkdir /api

WORKDIR /api

ADD ./api /api/

RUN pip install -r requirements.txt && \
    apk del .build-deps