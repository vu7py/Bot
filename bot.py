from telegram import Update
from telegram.ext import Application, CommandHandler
import os

# نجيب التوكن من المتغيرات البيئية في Railway
TOKEN = os.getenv("7545565077:AAFhr5slS9AxhCWAMgk_VQIZFFDf6HiJjqo")

async def start(update: Update, context):
    await update.message.reply_text("أهلاً 👋! أنا شغال على Railway 🚂")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()