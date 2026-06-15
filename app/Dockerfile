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

EXPOSE 8000

CMD ["/entrypoint.sh"]