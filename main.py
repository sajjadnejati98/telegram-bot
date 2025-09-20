import os
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update

TOKEN = os.environ.get("TOKEN", "").strip()

if not TOKEN:
    raise ValueError("توکن پیدا نشد!")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ربات روشنه ✅")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

if __name__ == "__main__":
    print("🚀 Bot is starting...")
    app.run_polling()
