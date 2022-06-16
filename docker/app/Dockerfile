FROM python:3.9

ARG app_dir=/app/

RUN apt update

ADD requirements.txt $app_dir

WORKDIR $app_dir

RUN pip install --upgrade pip

RUN pip install -r requirements.txt