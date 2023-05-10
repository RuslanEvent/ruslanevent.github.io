from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    update.message.reply_invoice()
    await update.message.reply_text("Let's make an order!", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(web_app='https://ruslanevent.github.io')]]))


app = ApplicationBuilder().token('5838841823:AAGUMz01lYyPqVBsTO-Xx9jvvDw7xcWD8Fo').build()
app.run_polling()