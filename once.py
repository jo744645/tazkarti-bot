# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# إعدادات تليجرام
BOT_TOKEN = "7204967716:AAGJZ5lGRqcn0DNR2zJelfRqCFpZOvGeN8U"
CHAT_ID = "1103230055"

# كلمات البحث
keywords = ["الأهلي", "Al Ahly", "Ahly", "AL-AHLY", "Al Ahly FC"]

# رابط الموقع
url = "https://www.tazkarti.com/#/matches"

def send_telegram_message(message):
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    try:
        requests.post(telegram_url, data=payload)
    except Exception as e:
        print("Telegram Error:", e)

def check_tickets():
    print("Checking tickets...")

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        time.sleep(5)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        text = soup.text.lower()

        if any(word.lower() in text for word in keywords) and "تم غلق الحجز" not in text:
            print("Tickets found!")
            send_telegram_message(
                "🎟️ تذاكر الأهلي متاحة الآن!\nhttps://www.tazkarti.com/#/matches"
            )
        else:
            print("No tickets.")

    except Exception as e:
        print("Error:", e)

    finally:
        driver.quit()

# تشغيل الفحص مرة واحدة
check_tickets()
