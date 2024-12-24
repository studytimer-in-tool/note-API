import os

class Config:
    LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
    DEFAULT_INTERVAL = 2  # 秒
