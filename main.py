from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler
import os
import logging

# ======== تنظیمات ========
TOKEN = os.getenv("TOKEN")  # توکن را از Environment Variables بخوان
if not TOKEN:
    raise ValueError("لطفاً TOKEN را در Environment Variables ست کنید!")

bot = Bot(token=TOKEN)
app = Flask(__name__)

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ===== Handler برای /start =====
def start(update, context):
    update.message.reply_text("سلام! ربات تستی فعال است ✅")

# ===== Dispatcher =====
dp = Dispatcher(bot, None, workers=0)
dp.add_handler(CommandHandler("start", start))

# ===== مسیر Webhook =====
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dp.process_update(update)
    return "OK"

# ===== مسیر Ping ساده =====
@app.route("/", methods=["GET"])
def index():
    return "Bot is alive ✅"

# ===== اجرا =====
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
