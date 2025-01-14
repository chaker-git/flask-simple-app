# syntax=docker/dockerfile:1

FROM python:3.11

WORKDIR /code

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 50505
EXPOSE 80
EXPOSE 8000

ENTRYPOINT ["gunicorn", "app:app"]
