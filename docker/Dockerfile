FROM python:3.9.13

USER root

COPY ./requirements.txt .
RUN python -m pip install --upgrade pip
RUN python -m pip install --upgrade setuptools
RUN python -m pip install wheel
RUN python -m pip install -r requirements.txt

WORKDIR /opt/app
