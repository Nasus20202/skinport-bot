FROM python:3.12.2-alpine

WORKDIR /app
COPY src/ .
COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

CMD ["python", "-u", "main.py"]
EXPOSE 5000