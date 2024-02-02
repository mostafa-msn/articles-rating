# pull official base image
FROM python:3.8-slim AS compile-image
LABEL maintainer="soltaninejad.msn@gmail.com"

# set work directory
RUN mkdir /code
WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get update && \
    apt-get install -yqq --no-install-recommends --show-progress \
    supervisor wget nano curl

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /code/
RUN pip install -r requirements.txt

# copy project
COPY . /code/
