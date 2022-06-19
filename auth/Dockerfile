FROM python:3-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn

COPY . .

RUN [ "gunicorn", "--bind=127.0.0.1:5000", "--workers=1", "auth:app" ]
