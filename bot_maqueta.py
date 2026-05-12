import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Configura el log para ver mensajes útiles
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING) # Silencia logs ruidosos de httpx

# Define el token de tu bot (¡REEMPLÁZALO CON TU TOKEN REAL!)
TOKEN = "8993099784:AAFAUsVR87UVAoWmzyT06gt0uLUwcay_h6g" # <--- ¡IMPORTANTE! Copia aquí tu token de BotFather

# Función que se ejecuta cuando el usuario envía /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        f"¡Hola, {user.mention_html()}! Soy tu bot de prueba. "
        "Para jugar, simplemente envíame un mensaje y te daré una 'moneda'."
    )

# Función que se ejecuta cuando el usuario envía un mensaje de texto
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("¡Aquí tienes una moneda de oro virtual! 💰")

def main() -> None:
    """Inicia el bot."""
    # Crea la aplicación y pásale el token de tu bot.
    application = Application.builder().token(TOKEN).build()

    # Agrega un manejador para el comando /start
    application.add_handler(CommandHandler("start", start))

    # Agrega un manejador para cualquier mensaje de texto que no sea un comando
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Inicia el polling (el bot estará escuchando nuevos mensajes)
    print("Bot iniciado. Esperando mensajes...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()