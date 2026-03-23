FROM python:3.11-slim

WORKDIR /app

COPY data_research/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY data_research/app.py app.py

CMD ["python", "app.py"]