# Stage 1: Build Angular App
FROM node:18-alpine AS frontend-builder

WORKDIR /frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ .
RUN npm run build

# Stage 2: Build Backend with FastAPI
FROM python:3.10-slim AS backend

WORKDIR /app
COPY backend/ /app/backend
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 3: Combine and run with supervisord
FROM python:3.10-slim

# Install nginx and supervisor
RUN apt-get update && \
    apt-get install -y nginx supervisor && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy backend and requirements
COPY --from=backend /app /app

# Copy Angular built files to NGINX
COPY --from=frontend-builder /frontend/dist/gustabor_frontend1/browser /var/www/frontend

# Copy NGINX config
COPY frontend/nginx.conf /etc/nginx/conf.d/default.conf

# Configure Supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose ports
EXPOSE 80 8000

# Run both NGINX and Uvicorn
CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
