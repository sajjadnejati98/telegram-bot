from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler,
    MessageHandler, filters, ContextTypes, ConversationHandler
)

# توکن ربات
TOKEN = "8208186251:AAHFwFdC5bRJkH8t2V-p7yOk-awOYWuKXAo"

# مراحل محاسبه
FIRST_NUMBER, OPERATION, SECOND_NUMBER = range(3)


# ===== /start =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام 👋\nمن روشنم ✅ برای شروع محاسبه دستور /calc رو بزن.")


# ===== شروع محاسبه =====
async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("عدد اول رو وارد کن:")
    return FIRST_NUMBER


async def first_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        context.user_data["first_number"] = float(update.message.text)
    except ValueError:
        await update.message.reply_text("❌ لطفاً یک عدد معتبر وارد کن.")
        return FIRST_NUMBER

    keyboard = [
        [
            InlineKeyboardButton("➕ جمع", callback_data="add"),
            InlineKeyboardButton("➖ تفریق", callback_data="sub"),
        ],
        [
            InlineKeyboardButton("✖️ ضرب", callback_data="mul"),
            InlineKeyboardButton("➗ تقسیم", callback_data="div"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("عمل مورد نظر رو انتخاب کن:", reply_markup=reply_markup)
    return OPERATION


async def operation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    context.user_data["operation"] = query.data
    await query.edit_message_text("عدد دوم رو وارد کن:")
    return SECOND_NUMBER


async def second_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        second = float(update.message.text)
        first = context.user_data["first_number"]
        op = context.user_data["operation"]

        if op == "add":
            result = first + second
        elif op == "sub":
            result = first - second
        elif op == "mul":
            result = first * second
        elif op == "div":
            if second == 0:
                await update.message.reply_text("❌ تقسیم بر صفر امکان‌پذیر نیست.")
                return ConversationHandler.END
            result = first / second
        else:
            result = "خطا در انتخاب عمل"

        await update.message.reply_text(f"✅ نتیجه: {result}")

    except ValueError:
        await update.message.reply_text("❌ لطفاً یک عدد معتبر وارد کن.")
        return SECOND_NUMBER

    return ConversationHandler.END


# ===== کنسل =====
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("محاسبه لغو شد ❌")
    return ConversationHandler.END


# ===== ران اصلی =====
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("calc", calc)],
        states={
            FIRST_NUMBER: [MessageHandler(filters.TEXT & ~filters.COMMAND, first_number)],
            OPERATION: [CallbackQueryHandler(operation)],
            SECOND_NUMBER: [MessageHandler(filters.TEXT & ~filters.COMMAND, second_number)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    app.add_handler(conv_handler)

    print("ربات Polling آماده است...")
    app.run_polling()


if __name__ == "__main__":
    main()
