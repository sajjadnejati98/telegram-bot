import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# گرفتن توکن از Environment (نه داخل کد)
TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ربات فعال است ✅")

def main():
    if not TOKEN:
        raise ValueError("❌ BOT_TOKEN تنظیم نشده یا مقدارش خالیه.")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
