FROM python:3.11-slim

WORKDIR /app

COPY web/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY web/app.py app.py
COPY web/templates templates
COPY web/static static

CMD ["python", "app.py"]