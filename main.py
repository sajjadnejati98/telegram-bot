from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# ======= TOKEN از Environment Variable =======
TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise ValueError("لطفاً TOKEN را در Environment Variables ست کنید!")

# ======= دستور /start =======
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! ربات تستی فعال است ✅")

# ======= ساخت اپلیکیشن و هندلر =======
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("✅ ربات Polling آماده است...")
app.run_polling()
