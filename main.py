import os
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = os.environ.get("TOKEN", "").strip()

print("TOKEN length:", len(TOKEN))
if not TOKEN or len(TOKEN) < 45:
    raise ValueError(f"❌ Invalid TOKEN: {TOKEN!r}")

async def start(update, context):
    await update.message.reply_text("ربات روشنه ✅")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

if __name__ == "__main__":
    print("🚀 Bot is starting...")
    app.run_polling()
