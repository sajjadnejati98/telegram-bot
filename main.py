import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram.error import InvalidToken, NetworkError

TOKEN = os.environ.get("TOKEN", "").strip()

if not TOKEN:
    raise ValueError("❌ TOKEN environment variable is empty or not set!")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ربات روشنه ✅")

async def run_bot():
    while True:
        app = None
        try:
            app = ApplicationBuilder().token(TOKEN).build()
            app.add_handler(CommandHandler("start", start))
            print("🚀 Bot is starting...")
            await app.run_polling()
        except InvalidToken as e:
            print(f"❌ Invalid Token! {e}")
            if app:
                await app.shutdown()
            print("💡 بررسی توکن و دوباره تلاش می‌کنیم در 10 ثانیه...")
            await asyncio.sleep(10)
        except NetworkError as e:
            print(f"⚠️ Network error: {e}")
            if app:
                await app.shutdown()
            print("💡 تلاش مجدد در 5 ثانیه...")
            await asyncio.sleep(5)
        except Exception as e:
            print(f"⚠️ خطای غیرمنتظره: {e}")
            if app:
                await app.shutdown()
            print("💡 تلاش مجدد در 5 ثانیه...")
            await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(run_bot())
