from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

MENTION_LIST = [
    "@evi1_pimp", "@Sansar3309", "@offflinne", "@altaiTratatai",
    "@Fjfhfkstifj", "@mariia_dark", "@Sm_Lil_i", "Тату",
    "@KKlepets", "@elena_linze", "@tarasovaalisa000"
]

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    text = update.message.text.lower()

    if 'свистать всех наверх' in text:
        mentions = ' '.join(MENTION_LIST)
        await update.message.reply_text(f"🚨 Призыв всех: {mentions}")

app = ApplicationBuilder().token("7789662269:AAG5hfbBLfoFfUlu3XpNAiiiTX-ij3zWrI0").build()
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

print("🤖 Бот запущен. Ожидает сообщение 'Свистать всех наверх'...")
app.run_polling()
