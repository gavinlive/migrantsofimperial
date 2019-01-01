# Dockerfile for migrantsofcatan
FROM ubuntu:16.04

MAINTAINER Your Name "gavin.live@live.co.uk"

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip python3-dev

RUN mkdir app

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "main.py" ]

EXPOSE 5000
