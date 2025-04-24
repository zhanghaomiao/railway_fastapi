FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create a script that runs migrations and starts the app
RUN echo '#!/bin/bash\n\
echo "Running database migrations..."\n\
alembic upgrade head\n\
echo "Starting application..."\n\
gunicorn app.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8080\n\
' > /app/start.sh && chmod +x /app/start.sh

# The Railway platform sets the PORT environment variable
CMD ["/app/start.sh"] 
