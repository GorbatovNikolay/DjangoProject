FROM python:alpine
WORKDIR /src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-client gcc musl-dev

RUN pip install --upgrade pip
COPY requirements.txt /src/
RUN pip install -r requirements.txt

COPY ./src /src/
