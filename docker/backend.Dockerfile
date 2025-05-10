FROM python:3.10-slim

WORKDIR /app

COPY gustabor_backend/ /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
