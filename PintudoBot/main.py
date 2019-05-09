# Projeto de Python!

# Criado por Henrique Kubinhetz em 08/05/2019
# encoding: UTF-8
# PintudoBot - O incrível bot que trata de fazer um sorteio muito esperado todos os dias!

# -----------------------------------------PATCH-NOTES---------------------------------------------

# ---- Versão 1.1 ----
# Funcional! Agora chamamos os migos pelo nome de usuário do Telegram!

# ---- Versão 1.0 ----
# Funcional! O bot está no grupo e responde bem às solicitações de pintudo. Parabéns aos envolvidos!


# --------------------------------------------TO-DO------------------------------------------------

# Funções de oi e tchau!
# Funções de ranking
# Limitação de tempo
# Tornar mais manejáveis os membros do grupo, com cadastro e edições... imagina se mais gente começa a usar?

# ---------------------------------------------CODE------------------------------------------------

# Agora quanto ao programa propriamente dito, let's begin!

# Fazendo as devidas importações:
from telegram.ext import Updater, CommandHandler
import requests
import re
import random

# Definição dos membros do grupo:
pintudos =\
{
    "1": "@120938790 (Henrique)",
    "2": "@pereiraarthur (Tuts)",
    "3": "@gustavoliveira (Gus)",
    "4": "@keyfp (Key)",
    "5": "@144361020 (Eriert)",
    "6": "@RealMr_Glasses (Nickolas)",
    "7": "@144164272 (Chuco)",
    "8": "@antoniobaiense (Tony)",
    "9": "@jardelvictor (Jardel)",
    "10": "@joaoemmanuel (Jão)",
    "11": "@wengbruch (Werner)"
}


# Função pintudo, que define o pintudo do dia.
def pintudo(bot,update):
    # Mostrando que a função foi chamada, cálculo aleatório e qual o resultado:
    print("Pintudo Request!")
    pintudo_id = str(random.randint(1, 11))
    print(pintudo_id)

    # Print do resultado e envio da mensagem:
    print("Parabéns, " + pintudos[pintudo_id] + "! " + "Você é o pintudo do dia!")
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="Parabéns, " + pintudos[pintudo_id] + "! " + "Você é o pintudo do dia!")


def teste(bot,update):
    # Função de teste, serve para verificar se o Bot está vivo!
    print("Função de teste!")
    chat_id = update.message.chat_id
    bot.send_message(chat_id = chat_id, text="Olá, estou aqui!")


def get_chat_id(bot,update):
    # Função de ID, serve para verificar qual o código da conversa! (Serve para fins de programação)
    print("Get Chat ID - On it!")
    chat_id = update.message.chat_id
    id_string = str(chat_id)
    bot.send_message(chat_id = chat_id, text="Olá! Seu chat id é: " + id_string)


# Função principal, que conecta ao Telegram e realiza as transações.
def main():
    updater = Updater('809699775:AAE5M1XZSAFCLa3DSQ7TMnORZ2HBI0EOxno')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('pintudo', pintudo))      # >>> Habilitação da função pintudo no bot.
    dp.add_handler(CommandHandler('teste', teste))          # >>> Habilitação da função de teste no bot.
    dp.add_handler(CommandHandler('getid', get_chat_id))   # >>> Habilitação da função de ID no bot.
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()


