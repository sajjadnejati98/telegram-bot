from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

# ====== توکن ربات ======
TOKEN = os.environ.get("TOKEN")  # یا مستقیماً بنویس "توکن_ربات"

# ====== دستور /start ======
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! ربات فعاله ✅")

# ====== تابع اصلی ربات ======
def main():
    # ساخت اپلیکیشن
    app = Application.builder().token(TOKEN).build()

    # اضافه کردن هندلر دستور /start
    app.add_handler(CommandHandler("start", start))

    print("ربات روشن شد ...")
    # شروع Polling
    app.run_polling()

# ====== اجرای ربات ======
if __name__ == "__main__":
    main()
