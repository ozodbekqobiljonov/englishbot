import os
import logging
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

app_flask = Flask(__name__)

@app_flask.route('/')
def home():
    return "Bot ishlayapti!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    await update.message.reply_text(
        f"Salom, {user_name}! English Vocabulary UZ botiga xush kelibsiz. Tez orada Ebbinghaus usulidagi so'z yodlash tizimi ishga tushadi!"
    )

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app_flask.run(host="0.0.0.0", port=port)

if __name__ == '__main__':
    import threading
    
    t = threading.Thread(target=run_flask)
    t.start()
    
    TOKEN = "9254081346:AAGdZz1PD_4ImqClg3GkCPH7joc-hTusJtY"
    
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    
    print("Bot polling rejimida ishga tushdi...")
    application.run_polling()
