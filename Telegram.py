import requests
import datetime
import time
from Settings import *
# Telegram bot token and chat ID
TOKEN = telegram_token
CHAT_ID = chat_id

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {'chat_id': CHAT_ID, 'text': text}
    response = requests.post(url, data=params)
    if response.status_code != 200:
        print(f"Failed to send message: {response.status_code}, {response.text}")

def schedule_messages(message_text):
    while True:
        now = datetime.datetime.now()
        # Check if it's time
        
        if now.hour == 7 and now.minute == 0:
            send_message(message_text)
            # Wait for the next day
            tomorrow = now + datetime.timedelta(days=1)
            next_time = datetime.datetime(tomorrow.year, tomorrow.month, tomorrow.day, 19, 0, 0)
            delta_seconds = (next_time - now).total_seconds()
            time.sleep(delta_seconds)
        else:
            # Check every minute
            time.sleep(60)

def main_tele(text):
    schedule_messages(text)

#if __name__ == '__main__':
    #main("Hello")
