import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    await update.message.reply_text(
        f"Salom, {user_name}! English Vocabulary UZ botiga xush kelibsiz. Tez orada Ebbinghaus usulidagi so'z yodlash tizimi ishga tushadi!"
    )

if __name__ == '__main__':
    TOKEN = "9254081346:AAGdZzlPD_4ImqClg3GkCPH7joqAdqie8zk"
    
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    print("Bot ishga tushdi...")
    app.run_polling()
