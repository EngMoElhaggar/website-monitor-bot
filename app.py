import requests
import time

# Telegram config
BOT_TOKEN = "7919366499:AAETZo3MLpyG6meOtJ_dk2nwbdnK0kPkds8"
CHAT_ID = "860256955"

# Website to monitor
URL = "https://london-innovation-academy.com"  # ← رابط موقعك الحقيقي

# Function to send Telegram message
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, data=data)
    except Exception as e:
        print(f"Error sending message: {e}")

# Monitoring loop
was_down = False

while True:
    try:
        response = requests.get(URL, timeout=10)
        if response.status_code == 200:
            if was_down:
                send_telegram_message("✅ الموقع رجع يشتغل ✅")
                was_down = False
        else:
            if not was_down:
                send_telegram_message(f"🚨 الموقع وقع! Status Code: {response.status_code}")
                was_down = True
    except requests.exceptions.RequestException:
        if not was_down:
            send_telegram_message("🚨 الموقع مش بيرد خالص! ممكن يكون واقع.")
            was_down = True

    time.sleep(60)  # بيراجع كل دقيقة
