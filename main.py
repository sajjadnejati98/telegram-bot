from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "توکن_اینجا"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام 👋 ربات دوباره فعاله ✅")

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
