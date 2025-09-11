import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
    ContextTypes,
    ConversationHandler,
)

# دریافت Token از متغیر محیطی
TOKEN = os.environ['TOKEN']

# مراحل ورودی
ENV, THICKNESS, DEPTH = range(3)

# شروع ربات و نمایش دکمه
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("محاسبه حجم مصرفی چسب (لیتر)", callback_data='calc_volume')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "سلام 👋\nلطفاً یکی از گزینه‌ها را انتخاب کنید:", reply_markup=reply_markup
    )

# هندلر انتخاب دکمه
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'calc_volume':
        await query.message.reply_text("محیط کل شیشه را به متر وارد کنید:")
        return ENV

# گرفتن محیط کل
async def get_env(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        context.user_data['env'] = float(update.message.text)
        await update.message.reply_text("ضخامت اسپیسر را به میلی‌متر وارد کنید:")
        return THICKNESS
    except ValueError:
        await update.message.reply_text("لطفاً عدد معتبر وارد کنید.")
        return ENV

# گرفتن ضخامت اسپیسر
async def get_thickness(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        context.user_data['thickness'] = float(update.message.text)
        await update.message.reply_text("عمق چسب زنی را به میلی‌متر وارد کنید:")
        return DEPTH
    except ValueError:
        await update.message.reply_text("لطفاً عدد معتبر وارد کنید.")
        return THICKNESS

# گرفتن عمق و محاسبه حجم
async def get_depth(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        depth = float(update.message.text)
        env = context.user_data['env']
        thickness = context.user_data['thickness']
        volume = (thickness * depth * env) / 1000
        await update.message.reply_text(f"✅ حجم مصرفی شما: {volume} لیتر")
        return ConversationHandler.END
    except ValueError:
        await update.message.reply_text("لطفاً عدد معتبر وارد کنید.")
        return DEPTH

# لغو عملیات
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❌ عملیات لغو شد.")
    return ConversationHandler.END

# ساخت اپلیکیشن
app = ApplicationBuilder().token(TOKEN).build()

# ConversationHandler با دکمه منو
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start), CallbackQueryHandler(button)],
    states={
        ENV: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_env)],
        THICKNESS: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_thickness)],
        DEPTH: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_depth)],
    },
    fallbacks=[CommandHandler('cancel', cancel)],
    allow_reentry=True
)

app.add_handler(conv_handler)

print("✅ ربات آماده و روشن شد...")
app.run_polling()
