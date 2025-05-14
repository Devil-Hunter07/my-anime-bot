import os
import telebot
import requests
import cloudscraper
import re

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)
scraper = cloudscraper.create_scraper()

video_pattern = r'https:\/\/[^\s]+\.m3u8'
subtitle_pattern = r'https:\/\/[^\s]+\.(vtt|srt|ass)'

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Yo! Mujhe hianimez.to ka episode link bhej, main tera video aur subtitle link nikaal ke dunga 🎬")

@bot.message_handler(func=lambda message: "hianimez.to" in message.text)
def extract_links(message):
    url = message.text.strip()
    bot.reply_to(message, "Scraping chalu hai... ⛏️")
    try:
        response = scraper.get(url)
        html = response.text

        video_match = re.findall(video_pattern, html)
        subtitle_match = re.findall(subtitle_pattern, html)

        if video_match:
            bot.send_message(message.chat.id, f"🎥 Video link:\n{video_match[0]}")
        if subtitle_match:
            bot.send_message(message.chat.id, f"📝 Subtitle link:\n{subtitle_match[0]}")
        if not video_match and not subtitle_match:
            bot.send_message(message.chat.id, "Kuch nahi mila bhai 😢 Link sahi se de ya page change ho gaya ho.")

    except Exception as e:
        bot.send_message(message.chat.id, f"⚠️ Error: {str(e)}")

bot.polling()
