FROM python:3.10-slim

WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV export FLASK_APP="app.py"
ENV export FLASK_ENV="development"

CMD flask run -h 0.0.0.0 -p 80