# Base image - Python 3.11 slim
FROM python:3.11-slim

# Sistem bağımlılıkları (OpenCV için)
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Çalışma dizini
WORKDIR /app

# Önce requirements kopyala (cache için)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını kopyala
COPY main.py .
COPY logger.py .
COPY yolo_model.py .
COPY best.pt .

# Log klasörü oluştur
RUN mkdir -p logs

# Port
EXPOSE 5757

# Çalıştır
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5757"]