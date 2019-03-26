FROM python:3.7.2
MAINTAINER brenden0730 <brenden0730@gmail.com>
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY . /app/
RUN pip3 install -r requirements.txt