FROM python:3

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1


WORKDIR /home/github

COPY requirements.txt /home/github/requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 8000/tcp