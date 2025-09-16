from flask import Flask, request
from telegram import Bot, Update
import logging

TOKEN = "8208186251:AAHFwFdC5bRJkH8t2V-p7yOk-awOYWuKXAo"
bot = Bot(token=TOKEN)
app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    if update.message and update.message.text == "/start":
        chat_id = update.message.chat.id
        bot.send_message(chat_id=chat_id, text="سلام! ربات تستی فعال است ✅")
    return "OK"

@app.route("/", methods=['GET'])
def index():
    return "Bot is alive ✅"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
