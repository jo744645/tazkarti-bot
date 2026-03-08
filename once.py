# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
import os

BOT_TOKEN = '7204967716:AAGJZ5lGRqcn0DNR2zJelfRqCFpZOvGeN8U'
CHAT_ID = '1103230055'

keywords = ["الأهلي", "Al Ahly", "Ahly", "AL-AHLY", "Al Ahly FC"]
url = "https://www.tazkarti.com/#/matches"

def send_telegram_message(message):
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(telegram_url, data=payload)
        print("✅ تم إرسال رسالة تليجرام")
    except Exception as e:
        print("❌ فشل إرسال الرسالة:", e)

def already_sent():
    return os.path.exists("sent.txt")

def mark_sent():
    with open("sent.txt", "w") as f:
        f.write("sent")

def check_tickets():
    print("⏳ جاري فحص موقع تذكرتي...")
    try:
        r = requests.get(url)
        page_text = r.text.lower()
        tickets_available = (
            any(word.lower() in page_text for word in keywords)
            and "تم غلق الحجز" not in page_text
        )

        if tickets_available and not already_sent():
            send_telegram_message(
                "🎟️ فتح حجز تذاكر ماتش الأهلي!\nاحجز من هنا:\nhttps://www.tazkarti.com/#/matches"
            )
            mark_sent()
            print("✅ تم إرسال الرسالة مرة واحدة فقط")
        else:
            print("لا يوجد جديد أو تم إرسال الرسالة مسبقًا")

    except Exception as e:
        print("⚠️ حدث خطأ أثناء الفحص:", e)

if __name__ == "__main__":
    check_tickets()
