FROM python:3-alpine
RUN adduser -D -h /home/divyarajput divyarajput
USER divyarajput
WORKDIR /home/divyarajput/portfolio

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .
CMD ["python", "-m", "uvicorn", "server:server", "--host", "0.0.0.0", "--port", "8080"]