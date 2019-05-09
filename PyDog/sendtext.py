# Estudo de Python!

# Criado por Henrique Kubinhetz em 08/05/2019
# encoding: UTF-8
# Nome da aula: sendtext

# Código simples para enviar texto!

from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re


def telegram_bot_sendtext(bot_message,update):
    bot_token = '809699775:AAE5M1XZSAFCLa3DSQ7TMnORZ2HBI0EOxno'
    bot_chatID = update.message.chat_id
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


test = telegram_bot_sendtext("Testing Telegram bot")
print(test)

