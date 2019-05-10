# Projeto de Python!

# Criado por Henrique Kubinhetz em 08/05/2019
# encoding: UTF-8
# PintudoBot - O incrível bot que trata de fazer um sorteio muito esperado todos os dias!

# -----------------------------------------PATCH-NOTES---------------------------------------------

# ---- Versão 1.2 ----
# Logging e Mensagens automáticas!

# ---- Versão 1.1 ----
# Funcional! Agora chamamos os migos pelo nome de usuário do Telegram!

# ---- Versão 1.0 ----
# Funcional! O bot está no grupo e responde bem às solicitações de pintudo. Parabéns aos envolvidos!


# --------------------------------------------TO-DO------------------------------------------------

# Ver se consigo usar a API do Telegram ao invés de requests para mensagens de startup e shutdown
# Funções de ranking
# Joguinhos e tokens para aumentar as chances de ganhar
# Limitação de tempo
# Tornar mais manejáveis os membros do grupo, com cadastro e edições... imagina se mais gente começa a usar?
# Entender as estruturas de logging
# Fazer funcionar a função de shutdown

# -------------------------------------------------------------------------------------------------
# ---------------------------------------------CODE------------------------------------------------
# -------------------------------------------------------------------------------------------------

# Agora quanto ao programa propriamente dito, let's begin!

# ------------------------------------------IMPORTAÇÕES--------------------------------------------

from telegram.ext import Updater, CommandHandler    # >>> Coisas de bot!
import random                                       # >>> Cálculos!
import logging                                      # >>> Logging de erros!
import requests                                     # >>> Para enviar mensagens grátis!

# --------------------------------------------LOGGING----------------------------------------------

# Sei lá o que isso faz...
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# ------------------------------------------DECLARAÇÕES--------------------------------------------

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

# Flags

timerflag = False   # >>> Flag para dizer que ainda não passou o tempo!

# Tokens!
bot_token = '809699775:AAE5M1XZSAFCLa3DSQ7TMnORZ2HBI0EOxno'  # PintudoBot
kubinha_chatID = '120938790'  # ID do Kubinha

# -------------------------------------FUNÇÕES SECUNDÁRIAS-----------------------------------------


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
    bot.send_message(chat_id=chat_id, text="Olá! Seu chat id é: " + id_string)

"""
def shutdown(bot,update):
    # Função de desligamento!
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="Vou nanar agora, boa noite!")
    Updater(bot_token).stop()
"""

def messenger(bot_message):

    send_text = 'https://api.telegram.org/bot' + bot_token + \
                '/sendMessage?chat_id=' + kubinha_chatID + \
                '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)
    return response.json()

# -------------------------------------------------------------------------------------------------
# ---------------------------------------------MAIN------------------------------------------------
# -------------------------------------------------------------------------------------------------

# Função principal, que conecta ao Telegram e realiza as transações.
def main():
    updater = Updater(bot_token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('pintudo', pintudo))       # >>> Habilitação da função pintudo no bot.
    dp.add_handler(CommandHandler('teste', teste))           # >>> Habilitação da função de teste no bot.
    dp.add_handler(CommandHandler('getid', get_chat_id))     # >>> Habilitação da função de ID no bot.
#    dp.add_handler((CommandHandler('shutdown', shutdown)))   # >>> Habilitação da função de shutdown.
    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    messenger("Olá, papai! Estou online! :D")
    main()


