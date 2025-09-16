from telegram.ext import Application, CommandHandler

# ✅ توکن واقعی از BotFather
TOKEN = "8208186251:AAHFwFdC5bRJkH8t2V-p7yOk-awOYWuKXAo"

app = Application.builder().token(TOKEN).build()

async def start(update, context):
    await update.message.reply_text("ربات روشنه ✅")

app.add_handler(CommandHandler("start", start))

print("ربات Polling آماده است...")
app.run_polling()
