from telegram.ext import Application, CommandHandler

# ✅ توکن واقعی از BotFather
TOKEN = "8208186251:AAE8HhwgpbGnawNcruZNzVHy-mSPqL5L2Bc"

app = Application.builder().token(TOKEN).build()

async def start(update, context):
    await update.message.reply_text("ربات روشنه ✅")

app.add_handler(CommandHandler("start", start))

print("ربات Polling آماده است...")
app.run_polling()
