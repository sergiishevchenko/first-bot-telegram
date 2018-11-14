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


@bot.message_handler(content_types=["commands"])
def handle_command(message):
    print("Пришла команда")


@bot.message_handler(content_types=["text"])
def handle_text(message):
    print("Пришло простое сообщение")


@bot.message_handler(content_types=["document"])
def handle_document(message):
    print("Пришёл документ")


@bot.message_handler(content_types=["audio"])
def handle_audio(message):
    print("Пришла аудиозапись")



bot.polling(none_stop=True, interval=0)