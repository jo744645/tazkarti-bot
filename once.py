# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os

BOT_TOKEN = '7204967716:AAGJZ5lGRqcn0DNR2zJelfRqCFpZOvGeN8U'
CHAT_ID = '1103230055'
URL = "https://www.tazkarti.com/#/matches"
KEYWORDS = ["الأهلي", "Al Ahly", "Ahly", "AL-AHLY", "Al Ahly FC"]
DATA_FILE = "sent_matches.txt"

def send_telegram(msg):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )

def load_sent_matches():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return set(line.strip() for line in f)
    return set()

def save_sent_match(match_name):
    with open(DATA_FILE, "a", encoding="utf-8") as f:
        f.write(match_name + "\n")

def check_matches():
    try:
        r = requests.get(URL)
        page_text = r.text.lower()

        sent_matches = load_sent_matches()
        # ابحث عن أي ماتش للكلمات المفتاحية
        new_matches = [kw for kw in KEYWORDS if kw.lower() in page_text and kw not in sent_matches]

        for match in new_matches:
            send_telegram(f"🎟️ فتح حجز تذاكر لماتش: {match}\nاحجز هنا:\n{URL}")
            save_sent_match(match)
            print(f"✅ تم إرسال رسالة لماتش: {match}")

        if not new_matches:
            print("لا توجد مباريات جديدة اليوم")

    except Exception as e:
        print("⚠️ حدث خطأ أثناء الفحص:", e)

if __name__ == "__main__":
    check_matches()
