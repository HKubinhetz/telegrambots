# Estudo de Python!

# Criado por Henrique Kubinhetz em 10/05/2019
# encoding: UTF-8
# Nome da aula: startupmessagin

import requests

def telegram_bot_sendtext(bot_message):

    # Tokens!
    bot_token = '809699775:AAE5M1XZSAFCLa3DSQ7TMnORZ2HBI0EOxno'         # PintudoBot
    kubinha_chatID = '120938790'                                        # ID do Kubinha

    send_text = 'https://api.telegram.org/bot' + bot_token +\
                '/sendMessage?chat_id=' + kubinha_chatID +\
                '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)
    return response.json()


telegram_bot_sendtext("Testing Telegram bot")
