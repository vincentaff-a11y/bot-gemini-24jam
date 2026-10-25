import os
import time
import schedule
import telebot
from google import genai

# --- GANTI TIGA TULISAN DI BAWAH PAKAI KUNCI KAMU ---
GEMINI_API_KEY = "AQ.Ab8RN6IplXqIGyhCe7mwFzUGD-j-eDIjFRmmuoMhWxNDx_nlYA"
TELEGRAM_BOT_TOKEN = "8658118716:AAGfu_h7GiWz624cwFkz34VQQdVFoGvsPi8"
TELEGRAM_CHAT_ID = "7522346825"

# Hubungkan ke Gemini & Telegram
client = genai.Client(api_key=GEMINI_API_KEY)
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

def tugas_otomatis():
    prompt = "Buatkan 1 ide postingan digital marketing yang singkat, menarik, dan kreatif untuk hari ini."
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt
    )
    
    pesan = f"🤖 **Laporan AI Agent 24 Jam**\n\n{response.text}"
    bot.send_message(TELEGRAM_CHAT_ID, pesan, parse_mode="Markdown")
    print("Berhasil kirim laporan ke Telegram!")

# Jadwal: Kirim pesan otomatis setiap jam 08:00 pagi
schedule.every().day.at("08:00").do(tugas_otomatis)

print("AI Agent siap dan berjalan 24 jam...")

while True:
    schedule.run_pending()
    time.sleep(60)