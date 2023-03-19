FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ["model.cbm", "app.py", "./"] .

ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:5000", "app:app" ]