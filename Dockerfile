FROM python:latest

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

COPY ./requirements.txt .
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED 1

COPY echo_server.py ./

CMD [ "python3", "/usr/src/app/echo_server.py"]