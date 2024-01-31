FROM ubuntu:22.04

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt update
RUN apt install -y python3
RUN apt install -y pip

RUN pip install -r requirements.txt

EXPOSE 8000

COPY . .

CMD ["python3", "app.py"]