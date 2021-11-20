FROM python:3

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1


WORKDIR /home/github

COPY _requirements.txt /home/github/_requirements.txt

RUN pip3 install -r _requirements.txt

EXPOSE 8000/tcp