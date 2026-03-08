# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os

# 🔹 إعدادات تليجرام
BOT_TOKEN = '7204967716:AAGJZ5lGRqcn0DNR2zJelfRqCFpZOvGeN8U'
CHAT_ID = '1103230055'

# 🔹 كلمات البحث
keywords = ["الأهلي", "Al Ahly", "Ahly", "AL-AHLY", "Al Ahly FC"]

# 🔹 رابط الموقع
url = "https://www.tazkarti.com/#/matches"

# 🔹 إعداد Selenium
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# 🔹 إرسال رسالة تليجرام
def send_telegram_message(message):
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(telegram_url, data=payload)
        print("✅ تم إرسال رسالة تليجرام")
    except Exception as e:
        print("❌ فشل إرسال الرسالة:", e)

# 🔹 للتحقق إن الرسالة اتبعت قبل كده
def already_sent():
    return os.path.exists("sent.txt")

def mark_sent():
    with open("sent.txt","w") as f:
        f.write("sent")

# 🔹 فحص الموقع
def check_tickets():
    print("⏳ جاري فحص موقع تذكرتي
