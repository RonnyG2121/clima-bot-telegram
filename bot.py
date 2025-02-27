# Este archivo es para crear las funciones del bot
from threading import Thread

import clima  # Es el módulo que contiene las funciones para consultar el clima
import os
import telebot

# Obteniendo el token de telegram
token = os.environ.get('telegram_token')

# print(token)

# Instanciando el bot
bot = telebot.TeleBot(token=token)

# Agregando manejadores de comandos. Esto se hace con decoradores


@bot.message_handler(commands=['start'])
def iniciar(message):
    bot.reply_to(message, """
    Hola, Te doy la bienvenida al bot del clima.
                 Para consultar el clima actual, escribe /c y el nombre de tu ciudad en inglés.
""")
    # print(message)

# Comando para consultar el clima
@bot.message_handler(commands=["c"])
def obtener_clima_actual(message):
    var_comando = message.text
    var_comando = var_comando.split()
    comando_clima= var_comando[1].lower()
    resultado_clima = clima.clima_actual(comando_clima)
    # print(cclimaomando_clima)
    # respuesta = "200"
    bot.send_chat_action(message.chat.id, "typing")
    # bot.send_message(message.chat.id, f"{message.from_user.first_name}")
    bot.reply_to(message, f"""
<b>{resultado_clima}</b>""", parse_mode="html")


# manejador de todo lo que no esta permitido
@bot.message_handler(content_types=['text', 'audio', 'document', 'photo', 'sticker', 'video', 'video_note', 'voice', 'location', 'contact'])
def bot_mensajes_texto(message):
    # Gestiona los mensajes de texto recibidos
    if message.text and message.text.startswith("/"):
        bot.send_chat_action(message.chat.id, "typing")
        bot.send_message(message.chat.id, "Comando no disponible")
    else:
        bot.send_chat_action(message.chat.id, "typing")
        bot.send_message(message.chat.id, "Comando no disponible")



def recibir_mensajes():
    # Bucle infinito que comprueba si hay nuevos mensajes en el bot
    bot.infinity_polling()



def main():
    # Por cada nuevo comando que agrego, se debe agregar el comando, y este rige el orden de los mismos.
    bot.set_my_commands([
        telebot.types.BotCommand("/start", "Menu Inicio"),
        telebot.types.BotCommand(
            "/c", "Devuelve el clima de la ciudad"),
        telebot.types.BotCommand(
            "/ayuda", "Muestra ejemplos de las consultas"),
    ])

    print('Iniciando " Bot"')
    hilo_bot = Thread(name="hilo_bot", target=recibir_mensajes)
    hilo_bot.start()
    print('Bot iniciado')


if __name__ == "__main__":
    main()
