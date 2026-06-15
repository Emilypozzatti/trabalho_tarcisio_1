FROM python:3.11-slim

WORKDIR /app

# dependências do sistema (IMPORTANTE)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# dependências python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# código
COPY . .

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]

# expõe porta
EXPOSE 8000

# gunicorn otimizado
CMD ["gunicorn", "todoproject.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]