import telebot
import constants
import os
import random
import urllib.request as urllib2

bot = telebot.TeleBot(constants.token)

# bot.send_message(486128297, "test")
# 48612897 - my id
#
# upd = bot.get_updates()
# print(upd)
# last_upd = upd[-1]
# message_from_user = last_upd.message
# print(message_from_user)

print(bot.get_me())


def log(message, answer):
    from datetime import datetime
    print(datetime.now())
    print("Message from {0} {1}. (id = {2}) \n Text - {3}".format(message.from_user.first_name,
                                                                  message.from_user.last_name,
                                                                  str(message.from_user.id),
                                                                  message.text))

    print(answer)


@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', '/stop')
    user_markup.row('photo', 'audio', 'docs')
    user_markup.row('sticker', 'video', 'voice', 'location')
    bot.send_message(message.from_user.id, 'Welcome..', reply_markup=user_markup)


@bot.message_handler(commands=['stop'])
def handle_stop(message):
    hide_markup = telebot.types.ReplyKeyboardMarkup()
    bot.send_message(message.from_user.id, '..', reply_markup=hide_markup)


@bot.message_handler(commands=["help"])
def handle_command(message):
    bot.send_message(message.chat.id, """Eeep! All right!""")


@bot.message_handler(content_types=["text"])
def handle_text(message):
    answer = "You are bad gamer!"
    if message.text == 'a':
        answer = "B"
        log(message, answer)
        bot.send_message(message.chat.id, "B")
    elif message.text == 'b':
        answer = "A"
        log(message, answer)
        bot.send_message(message.chat.id, "A")
    elif message.text == "1" or message.text == "2":
        bot.send_message(message.chat.id, "No! This is 1 or 2...")
    elif message.text == "1" and str(message.from_user.id) == "48612897":
        bot.send_message(message.chat.id, "Excellent!")
    else:
        bot.send_message(message.chat.id, answer)
        log(message, answer)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'photo':
        # directory = 'C:/....'
        # all_files_in_directory = os.listdir(directory)
        # random_file = random.choice(all_files_in_directory)
        # img = open(directory + '/' + random_file, 'rb')
        # bot.send_chat_action(message.from_user.id, 'upload photo')
        # bot.send_photo(message.from_user.id, img)
        # img.close()
        url ='https://goo.gl/58RCFF'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif 


# @bot.message_handler(content_types=["document"])
# def handle_document(message):
#     print("Пришёл документ")
#
#
# @bot.message_handler(content_types=["audio"])
# def handle_audio(message):
#     print("Пришла аудиозапись")
#
#
# @bot.message_handler(content_types=["photo"])
# def handle_photo(message):
#     print("Пришла фотография")
#
#
# @bot.message_handler(content_types=["sticker"])
# def handle_sticker(message):
#     print("Пришёл стикер")


bot.polling(none_stop=True, interval=0)