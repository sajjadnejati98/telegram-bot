from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from flask import Flask
import threading
import os

# ===== توکن ربات =====
TOKEN = os.getenv("BOT_TOKEN", "اینجا_توکن_ربات_بزار")

# ===== سرور Flask برای فعال نگه داشتن =====
app = Flask(__name__)

@app.route('/')
def home():
    return "ربات فعال است ✅"

def run_flask():
    app.run(host="0.0.0.0", port=8080)

# ===== هندلر تست =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام 👋 ربات روشن و فعال است ✅")

def main():
    # اجرای Flask در ترد جدا
    threading.Thread(target=run_flask).start()

    # اجرای ربات تلگرام
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == "__main__":
    main()
