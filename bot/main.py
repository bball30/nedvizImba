from telegram.ext import (
    ApplicationBuilder, CommandHandler,
    MessageHandler, ContextTypes, filters
)
from bot.handlers import start, address, handle_message, analytics
from bot.config import TELEGRAM_TOKEN
from analytics.db import init_db

def main():
    init_db()  # Создаёт таблицы
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("address", address))
    app.add_handler(CommandHandler("analytics", analytics))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
