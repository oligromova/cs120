import telebot

access_token = '1006276673:AAEDB5O1lczcYqKTlBbKexMgi6iHEPdqBqA'
telebot.apihelper.proxy = {'https': 'https://85.132.71.82:3128'}


bot = telebot.TeleBot(access_token)


@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling()
