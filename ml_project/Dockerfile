# syntax=docker/dockerfile:1
FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
RUN apt-get update && apt-get install -y libgl1
COPY deployment_req.txt /code/
RUN pip install -r deployment_req.txt
COPY . /code/