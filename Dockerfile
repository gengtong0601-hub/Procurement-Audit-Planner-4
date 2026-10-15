FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN useradd --create-home auditor && mkdir -p /app/runtime && chown -R auditor:auditor /app
USER auditor
ENV PORT=8000
EXPOSE 8000
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${PORT:-8000} --workers 1 --threads 8 --timeout 300 harness.app:app"]
