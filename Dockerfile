FROM python:3.12-slim

WORKDIR /XpenseMeter

COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

CMD ["uvicorn", "XpenseMeter.main:app", "--host", "0.0.0.0", "--port", "8000"]