FROM python:3-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn

COPY . .

EXPOSE 5000/tcp

CMD [ "gunicorn", "--bind=0.0.0.0:5000", "--workers=1", "auth:app" ]
