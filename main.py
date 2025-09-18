from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# ====== توکن ربات ======
TOKEN = "8208186251:AAGzIFLj64SmUCChEMHMyziZay5rd93X6Ns"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ ربات فعال است و درست کار می‌کند.")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
