FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
RUN pip install werkzeug==2.0.3
RUN pip install psutil

CMD ["python", "app.py"]
