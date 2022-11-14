# syntax=docker/dockerfile:1
From python:3.11.0rc1-alpine3.16
WORKDIR /home/django/dockproject
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python", "manage.py" , "runserver"]