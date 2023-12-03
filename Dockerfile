FROM python:3.10.0-alpine3.15

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000

CMD python ./app.py