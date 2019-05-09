# Projeto de Python!

# Criado por Henrique Kubinhetz em 08/05/2019
# encoding: UTF-8
# PyDog - O incrível bot que mostra fotos incríveis de cachorrinhos sob demanda!

# Let's begin!

from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater('809699775:AAE5M1XZSAFCLa3DSQ7TMnORZ2HBI0EOxno')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()





