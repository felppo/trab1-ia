import telebot
import os
import knn

API_TOKEN = '-----------'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(func=lambda m: True)
def welcome(message):
    bot.reply_to(message, "não tô a fim de papo. manda logo uma foto pra eu te liberar.")


@bot.message_handler(content_types=['photo'])
def photo_received(img):
    fileID = img.photo[-1].file_id
    fileInfo = bot.get_file(fileID)
    downloaded_file = bot.download_file(fileInfo.file_path)

    with open("photo.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)

    check = knn.proc_received_photo("photo.jpg")
    os.remove("photo.jpg")
    if check == -1:
        bot.reply_to(img, "poh, manda uma foto melhorzinha")
    elif check == 1:
        bot.reply_to(img, "pode entrar, chefia.")
    elif check == 0:
        bot.reply_to(img, "vaza daqui antes que eu chame a polícia")


bot.polling()
