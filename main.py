from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler
import logging

TOKEN = "8208186251:AAHFwFdC5bRJkH8t2V-p7yOk-awOYWuKXAo"
bot = Bot(token=TOKEN)
app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ====== Handler for /start ======
def start(update, context):
    update.message.reply_text("سلام! ربات تستی فعال است ✅")

# ====== Dispatcher ======
dp = Dispatcher(bot, None, workers=0)
dp.add_handler(CommandHandler("start", start))

# ====== Webhook route ======
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dp.process_update(update)
    return "OK"

# ====== Ping route ======
@app.route("/", methods=["GET"])
def index():
    return "Bot is alive ✅"

# ====== Run Flask ======
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
