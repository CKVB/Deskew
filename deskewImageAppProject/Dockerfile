FROM ubuntu:18.04

ENV DEBIAN_FRONTEND="noninteractive"\
	FLASK_ENV=production

COPY . /deskewAppProject
WORKDIR /deskewAppProject

RUN apt-get update &&\
	apt-get remove -y &&\
	apt-get -y install --no-install-recommends --yes python3.6 &&\
	apt-get -y install --no-install-recommends --yes python3-pip &&\
	apt-get -y install --no-install-recommends --yes python3-setuptools &&\
	apt-get -y install --no-install-recommends --yes python3-opencv &&\
	python3 -m pip install --upgrade pip &&\
	pip3 install -r requirements.txt &&\
	apt-get clean &&\
	rm -rf /var/cache/apt/* &&\
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD ["/bin/bash", "entrypoint.sh"]
