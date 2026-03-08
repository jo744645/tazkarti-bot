-- coding: utf-8 --

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

إعدادات تليجرام

BOT_TOKEN = '7204967716:AAGJZ5lGRqcn0DNR2zJelfRqCFpZOvGeN8U'
CHAT_ID = '1103230055'

كلمات البحث

keywords = ["الأهلي", "Al Ahly", "Ahly", "AL-AHLY", "Al Ahly FC"]

رابط الموقع

url = "https://www.tazkarti.com/#/matches"

إعداد Selenium

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

def send_telegram_message(message):
telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {"chat_id": CHAT_ID, "text": message}
try:
requests.post(telegram_url, data=payload)
print("✅ تم إرسال رسالة تليجرام")
except Exception as e:
print("❌ فشل إرسال الرسالة:", e)

def check_tickets():
print("⏳ جاري فحص موقع تذكرتي...")

driver = None  
try:  
    driver = webdriver.Chrome(options=options)  
    driver.get(url)  

    # وقت بسيط للتحميل  
    time.sleep(3)  

    soup = BeautifulSoup(driver.page_source, "html.parser")  
    page_text = soup.text.lower()  

    tickets_available = (  
        any(word.lower() in page_text for word in keywords)  
        and "تم غلق الحجز" not in page_text  
    )  

    if tickets_available:  
        print("🎟️ تم العثور على تذاكر للأهلي!")  
        send_telegram_message(  
            "🎟️ فيه تذاكر متاحة لمباريات الأهلي!\nاحجز بسرعة:\nhttps://www.tazkarti.com/#/matches"  
        )  
    else:  
        print("❌ لا توجد تذاكر متاحة حاليًا.")  

except Exception as e:  
    print("⚠️ حدث خطأ أثناء الفحص:", e)  

finally:  
    if driver:  
        driver.quit()

if name == "main":
check_tickets()
