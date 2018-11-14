import telebot
import constants

bot = telebot.TeleBot(constants.token)

bot.send_message(486128297, "test")
# 48612897 - my id

upd = bot.get_updates()
print(upd)
last_upd = upd[-1]
message_from_user = last_upd.message
