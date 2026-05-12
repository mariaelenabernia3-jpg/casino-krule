import os
import logging
from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# --- CONFIGURACIÓN DE FLASK PARA ENGAÑAR A RENDER ---
app = Flask('')

@app.route('/')
def home():
    return "El bot está vivo!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
# ---------------------------------------------------

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Pon tu token aquí para la prueba, o usa la variable de entorno
TOKEN = "8993099784:AAFAUsVR87UVAoWmzyT06gt0uLUwcay_h6g"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"¡Hola {update.effective_user.first_name}! Estoy corriendo gratis en la nube.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("¡Aquí tienes tu moneda virtual! 💰")

def main() -> None:
    # Iniciar el servidor web falso antes del bot
    keep_alive()
    
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    print("Bot iniciado...")
    application.run_polling()

if __name__ == "__main__":
    main()