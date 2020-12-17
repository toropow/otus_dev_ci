FROM python:3.7-buster
MAINTAINER toropow@gmail.com

WORKDIR /app

COPY requirements.txt ./
COPY book_shop ./
COPY .git ./

RUN pip install -r requirements.txt

EXPOSE 8000