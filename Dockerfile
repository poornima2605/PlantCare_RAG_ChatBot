FROM python:3.9
ENV PYTHONPATH=/app

WORKDIR /app

COPY requirements.txt .
COPY vector.index documents.pkl ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ app/


CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]
