import telebot
import constants
import os
import random
import urllib.request as urllib2

bot = telebot.TeleBot(constants.token)

bot.send_message(486128297, "test")
# 48612897 - my id

upd = bot.get_updates()
print(upd)
last_upd = upd[-1]
message_from_user = last_upd.message
print(message_from_user)

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
        url ='https://goo.gl/58RCFF'
        urllib2.urlretrieve(url, 'url_image.jpg')
        img = open('url_image.jpg', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text == 'audio':
        audio = open("C:/Users/....", "rb")
        bot.send_chat_action(message.from_user.id, 'upload audio')
        bot.send_audio(message.from_user.id, audio)
        audio.close()
    elif message.text == 'document':
        directory = 'C:/....'
        all_files_in_directory = os.listdir(directory)
        for files in all_files_in_directory:
            document = open(directory + '/' + files, "rb")
            bot.send_chat_action(message.from_user.id, 'upload document')
            bot.send_document(message.from_user.id, document)
            document.close()
    elif message.text == 'sticker':
        bot.send_sticker(message.from_user.id, constants.template_sticker_id)
    elif message.text == 'video':
        video = open("C:/....", "rb")
        bot.send_chat_action(message.from_user.id, 'upload video')
        bot.send_video(message.from_user.id, video)
        video.close()
    elif message.text == 'voice':
        voice = open("C:/....", "rb")
        bot.send_chat_action(message.from_user.id, 'upload voice')
        bot.send_voice(message.from_user.id, voice)
        voice.close()
    elif message.text == 'location':
        bot.send_chat_action(message.from_user.id, 'find_location')
        bot.send_location(message.from_user.id, 54.22544, 84.54585)


bot.polling(none_stop=True, interval=0)
