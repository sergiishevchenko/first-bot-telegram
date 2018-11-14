import telebot
import constants

bot = telebot.TeleBot(constants.token)

# bot.send_message(486128297, "test")
# 48612897 - my id
#
# upd = bot.get_updates()
# print(upd)
# last_upd = upd[-1]
# message_from_user = last_upd.message
# print(message_from_user)


@bot.message_handler(commands=["help"])
def handle_command(message):
    bot.send_message(message.chat.id, """Eeep! All right!""")


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == 'a':
        bot.send_message(message.chat.id, "B")
    elif message.text == 'b':
        bot.send_message(message.chat.id, "A")
    else:
        bot.send_message(message.chat.id, "Oopps!")


@bot.message_handler(content_types=["document"])
def handle_document(message):
    print("Пришёл документ")


@bot.message_handler(content_types=["audio"])
def handle_audio(message):
    print("Пришла аудиозапись")


@bot.message_handler(content_types=["photo"])
def handle_photo(message):
    print("Пришла фотография")


@bot.message_handler(content_types=["sticker"])
def handle_sticker(message):
    print("Пришёл стикер")


bot.polling(none_stop=True, interval=0)