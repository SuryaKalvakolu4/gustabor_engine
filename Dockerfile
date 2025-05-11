# --- FRONTEND BUILD PHASE ---
FROM node:18-alpine AS frontend-builder

WORKDIR /frontend
COPY gustabor_frontend1/package*.json ./
RUN npm install

COPY gustabor_frontend1/ ./
RUN npm run build

# --- BACKEND BUILD PHASE ---
FROM python:3.10-slim AS backend

WORKDIR /app
COPY gustabor_backend/ /app
COPY gustabor_backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --- FINAL IMAGE ---
FROM nginx:alpine

# Copy frontend
COPY --from=frontend-builder /frontend/dist/gustabor_frontend1/browser /usr/share/nginx/html

# Copy backend
COPY --from=backend /app /app

# Copy NGINX config
COPY gustabor_frontend1/nginx.conf /etc/nginx/conf.d/default.conf

# Copy Supervisor to run both frontend (nginx) and backend (uvicorn)
COPY supervisor.conf /etc/supervisor/conf.d/supervisor.conf

# Install supervisor and Python for backend
RUN apk add --no-cache bash supervisor python3 py3-pip

EXPOSE 80
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisor.conf"]
