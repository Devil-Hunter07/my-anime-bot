import os
from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text("Yo! Mujhe hianimez.to ka episode link bhej...")

def main():
    token = os.environ.get("BOT_TOKEN")
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
