from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8208186251:AAGhImACKTeAa1pKT1cVSQEsqp0Vo2yk-2o"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ربات فعال است ✅")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    print("🚀 Bot is starting...")
    app.run_polling()  # بدون asyncio.run()

if __name__ == "__main__":
    main()
