FROM python:3.7-buster
MAINTAINER toropow@gmail.com

WORKDIR /app

ENV SECRET_KEY='i)a3k2()raxl3z-*s@fvg=2k0sc_neyr#mc7hhc7z32y%$=e-d'
ENV DEBUG=True
ENV PG_USER=user
ENV PG_PASSWORD=password
ENV PG_DB_NAME=demo
ENV PG_HOST=127.0.0.1
ENV PG_PORT=5432
ENV COVERALLS_REPO_TOKEN=aQYVY11iG7BpRgItY0JTWawOdGdwafDDc

COPY requirements.txt ./
COPY book_shop ./

RUN pip install -r requirements.txt

EXPOSE 8000