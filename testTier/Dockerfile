FROM ubuntu:22.04

COPY . /app

RUN apt update
RUN apt install -y python3

CMD ["python3", "./app/index.py"]