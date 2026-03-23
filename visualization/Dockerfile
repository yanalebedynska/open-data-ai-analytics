FROM python:3.11-slim

WORKDIR /app

COPY visualization/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY visualization/app.py app.py

CMD ["python", "app.py"]