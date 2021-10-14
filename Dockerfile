FROM debian:stable-slim

RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y dist-upgrade
RUN DEBIAN_FRONTEND=noninteractive apt-get -yq install net-tools nginx python3-pip gunicorn
RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./lumiobytenet /lumiobytenet
COPY ./manage.py /lumiobytenet/

WORKDIR /lumiobytenet

COPY ./entrypoint.sh /lumiobytenet/
ENTRYPOINT ["sh", "./entrypoint.sh"]