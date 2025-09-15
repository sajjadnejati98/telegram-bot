import os
from threading import Thread
from flask import Flask
from telegram import Bot
from telegram.ext import Updater, CommandHandler

# ====== Flask app برای Ping UptimeRobot ======
app = Flask(__name__)

@app.route('/')
def home():
    return 'OK'

def run_flask():
    app.run(host='0.0.0.0', port=8000)

# اجرای Flask در Thread جداگانه
Thread(target=run_flask).start()

# ====== کد ربات تلگرام ======
TOKEN = os.environ.get("TOKEN")  # توکن ربات از Environment Variable

updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

# مثال ساده: دستور /start
def start(update, context):
    update.message.reply_text('سلام! ربات تست روشنه.')

dispatcher.add_handler(CommandHandler('start', start))

# شروع ربات
updater.start_polling()
updater.idle()
