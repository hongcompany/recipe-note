FROM python:3.7.2
MAINTAINER brenden0730 <brenden0730@gmail.com>
ENV PYTHONUNBUFFERED 1
WORKDIR .
COPY requirements.txt .
RUN pip3 install -r requirements.txt