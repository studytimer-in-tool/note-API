import time
from linebot import LineBotApi
from linebot.models import TextSendMessage
import os
from dotenv import load_dotenv

# 環境変数の読み込み
load_dotenv()

LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

def send_note_messages(user_id, notes, interval):
    """
    指定したユーザーにノートを連続送信する。
    """
    for note in notes:
        line_bot_api.push_message(user_id, TextSendMessage(text=note))
        time.sleep(interval)
