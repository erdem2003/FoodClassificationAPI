import logging
from logging.handlers import TimedRotatingFileHandler
import os

os.makedirs("logs", exist_ok=True)

handler = TimedRotatingFileHandler(
    filename="logs/app.log",
    when="midnight",        # her gece yarısı yeni dosya
    interval=30,            # 30 günde bir
    backupCount=12,         # 12 ay tut, eskiyi sil
    encoding="utf-8"
)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)
handler.setFormatter(formatter)

logger = logging.getLogger("yolo_api")
logger.setLevel(logging.INFO)
logger.addHandler(handler)