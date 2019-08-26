# Projeto de Python!

# Criado por Henrique Kubinhetz em 08/05/2019
# encoding: UTF-8
# PintudoBot - O incrível bot que trata de fazer um sorteio muito esperado todos os dias!

# -----------------------------------------PATCH-NOTES---------------------------------------------

# ---- Versão 1.3 ----
# Agora temos timing e migos em um arquivo! Nice!

# ---- Versão 1.2 ----
# Logging e Mensagens automáticas!

# ---- Versão 1.1 ----
# Funcional! Agora chamamos os migos pelo nome de usuário do Telegram!

# ---- Versão 1.0 ----
# Funcional! O bot está no grupo e responde bem às solicitações de pintudo. Parabéns aos envolvidos!


# --------------------------------------------TO-DO------------------------------------------------

# Fazer o bot xingar os outros aleatoriamente (fazer uma função randomigo)
# Fazer funcionar a função de shutdown
# Funções de ranking
# Joguinhos e tokens para aumentar as chances de ganhar
# Entender as estruturas de logging de erros

# -------------------------------------------------------------------------------------------------
# ---------------------------------------------CODE------------------------------------------------
# -------------------------------------------------------------------------------------------------

# Agora quanto ao programa propriamente dito, let's begin!

# ------------------------------------------IMPORTAÇÕES--------------------------------------------

from telegram.ext import Updater, CommandHandler    # >>> Coisas de bot!
import random                                       # >>> Cálculos!
import logging                                      # >>> Logging de erros!
import requests                                     # >>> Para enviar mensagens grátis!
from PintudoBot.timing.gettime import *             # >>> Para gerenciar o tempo!
from PintudoBot.filemanager.playerlist import *     # >>> Para gerenciar os usuários!

# --------------------------------------------LOGGING----------------------------------------------

# Sei lá o que isso faz...
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# ------------------------------------------DECLARAÇÕES--------------------------------------------

# Variáveis avulsas:

timelimit_value = 0             # Definição da variável de limite de tempo!

# Tokens!
bot_token = '809699775:AAE5M1XZSAFCLa3DSQ7TMnORZ2HBI0EOxno'  # PintudoBot
kubinha_chatID = '120938790'  # ID do Kubinha

# -------------------------------------FUNÇÕES SECUNDÁRIAS-----------------------------------------


# Função pintudo, que define o pintudo do dia.
def pintudo(bot=None, update=None):
    pintudos = playerlist_read()

    # Mostrando que a função foi chamada, cálculo aleatório e qual o resultado:
    print("Pintudo Request!")
    pintudo_id = str(random.randint(1, 11))

    # Print do resultado e envio da mensagem:
    print("Parabéns, " + pintudos[pintudo_id] + "! " + "Você é o pintudo do dia!")
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="Parabéns, " + pintudos[pintudo_id] + "! " + "Você é o pintudo do dia!")


# Função wait, que envia uma mensagem para esperar caso o tempo limite ainda não tenha sido atingido.
def wait(shotcalling_message, bot=None, update=None):
    print("Função wait() ativada!")
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=shotcalling_message)
    # to-do: incluir o tempo que falta na mensagem!


# Função shotcaller, que decide se elege o pintudo do dia ou espera mais um pouco.
def shotcaller(bot,update):
    print("Função shotcaller() ativada!")
    shotcalling_flag, shotcalling_message = gettime()
    print(shotcalling_message)
    if shotcalling_flag:
        pintudo(bot,update)
    else:
        wait(shotcalling_message, bot,update)


# Função timelimit, que mostra qual o tempo limite existente.
def timelimit(bot, update):

    global timelimit_value

    timelimit_value, timelimit_message = get_timelimit()
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=timelimit_message)
    bot.send_message(chat_id=chat_id, text="Para saber os comandos desse bot super completo (euzinho), digite /help")


# Função timelimit, que mostra qual o tempo limite existente.
def helpme(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="Lá vem você me amolar pedindo ajuda né? Oh well, como eu sou uma máquina "
                                           "desprovida de emoções, não faz diferença quantas vezes você chama esse"
                                           "comando. Vai da consciência de cada um (viu, @keyfp???) Pois bem:")
    bot.send_message(chat_id=chat_id, text="/pintudo - Razão da minha existência. Vamos eleger um pintudo! \n"
                                           "/teste - Será que estou vivo? Descubra com esse comando. \n"
                                           "/getid - Quer descobrir seu chat ID por qualquer motivo? Fique à vontade,"
                                           "mas não me envolva em nada além disso! Já basta meu mestre ser amigo do "
                                           "@144361020 (Eriert).\n"
                                           "/timelimit - Use esse para saber qual o tempo limite entre sorteios!\n"
                                           "/help - Tu tá de sacanagem se não sabe pra que serve esse.")


# Função timemanager, que muda o tempo limite sob demanda.
def timemanager(bot, update, args):
    chat_id = update.message.chat_id  # Paga o ID do chat para a mensagem logo em seguida.

    try:
        print("timemanager!")
        print(args)                                             # Listagem do que veio depois do comando.

        timelimit = changelimit(int(args[0]))                   # Aqui se faz a conversão e altera o limite pela função.

        # Mensagem de sucesso na alteração.
        bot.send_message(chat_id=chat_id, text="DEU CERTO!!! O novo limite é de " + str(timelimit) + " segundos.")
    except (IndexError, ValueError):
        global timelimit_value
        print("Erro na hora de mudar o tempo!")
        # Mensagem de insucesso na alteração.
        timelimit_value, timelimit_message = get_timelimit()
        bot.send_message(chat_id=chat_id, text="Difícil você fazer alguma coisa certo, né? (eu estou olhando pra você, "
                                               "@144164272 (Chuco)? O limite se mantém em: " + str(timelimit_value) +
                                               " segundos.")
        bot.send_message(chat_id=chat_id, text="Falando sério agora, certifique-se que você usou o comando"
                                               " corretamente: /timemanager <número de segundos> (sem as chaves, né?).")


# Função de teste, serve para verificar se o Bot está vivo!
def teste(bot,update):
    print("Função de teste!")
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="Olá, estou aqui! :D")


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
    dp.add_handler(CommandHandler('pintudo', shotcaller))       # >>> Habilitação da função pintudo no bot.
    dp.add_handler(CommandHandler('teste', teste))              # >>> Habilitação da função de teste no bot.
    dp.add_handler(CommandHandler('help', helpme))              # >>> Habilitação da função de ajuda no bot.
    dp.add_handler(CommandHandler('timelimit', timelimit))      # >>> Habilitação da função de tempo limite no bot.
    dp.add_handler(CommandHandler('getid', get_chat_id))        # >>> Habilitação da função de ID no bot.

    dp.add_handler(CommandHandler('changetime', timemanager, pass_args=True))       # >>> Habilitação da função de
                                                                                    # gestão de tempo no bot.

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    messenger("Olá, papai! Estou online! :D")
    main()


