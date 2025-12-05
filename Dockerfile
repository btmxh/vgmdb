FROM python:3.12-slim

# System deps (nginx optional — remove if your web app doesn’t need it)
# RUN apt-get update && apt-get install -y --no-install-recommends \
#         build-essential \
#     && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python deps
COPY pyproject.toml /app/pyproject.toml
RUN pip install --no-cache-dir .

# Copy code
COPY vgmdb /app/vgmdb
COPY run.py /app/run.py
COPY wsgi.py /app/wsgi.py

COPY static /app/www_root/static
COPY raml   /app/www_root/raml
COPY schema /app/www_root/schema
COPY static/robots.txt /app/www_root/robots.txt

COPY docker/sv-celery-background /app/sv-celery-background
COPY docker/sv-celery-priority /app/sv-celery-priority
RUN chmod +x /app/sv-celery-background /app/sv-celery-priority

# Default command: run the web app
CMD ["gunicorn", "vgmdb.main:app", "--worker-class", "gevent", "--workers", "4", "--bind", "0.0.0.0:80"]
