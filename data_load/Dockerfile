FROM python:3.11-slim

WORKDIR /app

COPY data_load/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY data_load/app.py app.py

CMD ["python", "app.py"]