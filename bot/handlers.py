from telegram import Update
from telegram.ext import ContextTypes
from bot.state import user_state
from analytics.db import SessionLocal
from analytics.models import Listing

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏠 Привет! Я бот НедвижИмба.\n"
        "Введи /address чтобы указать адрес интересующей недвижимости.\n"
        "Затем используй /analytics — и я пришлю аналитику по похожим объектам."
    )


async def address(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📝 Введи интересующий адрес:")
    user_state[update.effective_user.id] = "awaiting_address"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    if user_state.get(uid) == "awaiting_address":
        address_text = update.message.text
        context.user_data["address"] = address_text
        user_state[uid] = "address_received"
        await update.message.reply_text(
            f"✅ Адрес принят: {address_text}\nИспользуй /analytics для получения отчета.")
    else:
        await update.message.reply_text("⚠️ Не понял команду. Напиши /start чтобы начать сначала.")


async def analytics(update: Update, context: ContextTypes.DEFAULT_TYPE):
    address = context.user_data.get("address")
    if not address:
        await update.message.reply_text("📍 Сначала введи адрес через /address")
        return

    await update.message.reply_text(f"🔍 Выполняется анализ объектов рядом с: {address}...")

    # Пример запроса к БД
    db = SessionLocal()
    listings = db.query(Listing).filter(Listing.address.contains(address)).limit(5).all()

    if listings:
        response = f"📊 Найдено {len(listings)} объектов по адресу «{address}»:\n"
        for l in listings:
            response += f"- {l.title} — {l.price}₽ ({l.area} м²)\n"
        await update.message.reply_text(response)
    else:
        await update.message.reply_text("🙁 Пока нет данных по этому адресу (заглушка).")

    # Попытка отправить файл аналитики
    try:
        await update.message.reply_document(document=open("reports/analytics_template.xlsx", "rb"))
    except Exception:
        await update.message.reply_text("❌ Не удалось найти файл аналитики.")
