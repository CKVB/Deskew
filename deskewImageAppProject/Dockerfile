FROM ubuntu:18.04

ENV DEBIAN_FRONTEND="noninteractive"\
	FLASK_ENV=development

COPY . /deskewAppProject
WORKDIR /deskewAppProject

RUN apt-get update &&\
	apt-get -y install python3.6.2 &&\
	apt-get -y install python3-pip &&\
	apt-get -y install python3-opencv &&\
	python3 -m pip install --upgrade pip &&\
	pip3 install -r requirements.txt &&\
	rm -rf /var/cache/apt/*

CMD gunicorn --workers=5 --bind 0.0.0.0:5000 wsgi:app
