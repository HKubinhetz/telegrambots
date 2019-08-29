# Projeto de Python!

# Criado por Henrique Kubinhetz em 08/05/2019
# encoding: UTF-8
# PintudoBot - O incrível bot que trata de fazer um sorteio muito esperado todos os dias!

# -----------------------------------------PATCH-NOTES---------------------------------------------

# ---- Versão 1.5 ----
# Demorou, mas foi: Temos safe shutdown no bot!

# ---- Versão 1.4 ----
# Função randomigo para escolher pessoas aleatoriamente, seja nas mensagens, seja na função pintudo.

# ---- Versão 1.3 ----
# Agora temos timing e migos em um arquivo! Nice!

# ---- Versão 1.2 ----
# Logging e Mensagens automáticas!

# ---- Versão 1.1 ----
# Funcional! Agora chamamos os migos pelo nome de usuário do Telegram!

# ---- Versão 1.0 ----
# Funcional! O bot está no grupo e responde bem às solicitações de pintudo. Parabéns aos envolvidos!


# --------------------------------------------TO-DO------------------------------------------------

# Entender as estruturas de logging de erros
# Criar funções de ranking!
# Criar (ou inteligar) joguinhos e "tokens" para aumentar as chances de ganhar

# -------------------------------------------------------------------------------------------------
# ---------------------------------------------CODE------------------------------------------------
# -------------------------------------------------------------------------------------------------

# Agora quanto ao programa propriamente dito, let's begin!

# ------------------------------------------IMPORTAÇÕES--------------------------------------------

print("---------- Pintudo Bot v1.5 -----------")
print("----- Feito com amor pelo Kubinha -----")
print("Inicializando...")

from telegram.ext import Updater, CommandHandler    # >>> Coisas de bot!
import random                                       # >>> Cálculos!
import logging                                      # >>> Logging de erros!
import requests                                     # >>> Para enviar mensagens grátis!
import threading                                    # >>> Para desligar o bot em uma thread nova! (sei lá pq)
from PintudoBot.timing.gettime import *             # >>> Para gerenciar o tempo!
from PintudoBot.filemanager.playerlist import *     # >>> Para gerenciar os usuários!
print("Importações OK")
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
updater = Updater(bot_token) # atribuição do bot às atualizações
print("Declarações e conexão OK")
# -------------------------------------FUNÇÕES SECUNDÁRIAS-----------------------------------------


# Função pintudo, que define o pintudo do dia.
def pintudo(bot, update):

    pintudo_player = randomigo()
    # Print do resultado e envio da mensagem:
    print("Parabéns, " + pintudo_player + "! " + "Você é o pintudo do dia!")
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="Parabéns, " + pintudo_player + "! " + "Você é o pintudo do dia!")


# Função Randomigo, para eleger alguém aleatoriamente (usado em mensagens e na função pintudo)
def randomigo():
    playerlist = playerlist_read()      # Pega os nomes dos migos

    print("Randomigo Request!")             # Escolha de um número aleatório para pegar uma pessoa da lista.
    player_id = str(random.randint(1, 11))
    player = str(playerlist[player_id])
    return player


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
    timelimit_player = randomigo()      # Vamos escolher alguém para zoar!

    timelimit_value = get_timelimit()
    timelimit_message = "O tempo limite atual é de " + timelimit_value + " segundos. Nada tema! Você, usuário fresco " \
                        "e mau perdedor, pode agora mudar esse valor através do comando /changetime <segundos>. " \
                        "Se meu mestre (aquele gostoso) estiver com paciência, saberei até contar em minutos," \
                        " horas e até mesmo dias no futuro ! É mais do que se pode esperar, por exemplo, " \
                        "do " + timelimit_player + "."

    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=timelimit_message)
    bot.send_message(chat_id=chat_id, text="Para saber os comandos desse bot super completo (euzinho), digite /help")


# Função timelimit, que mostra qual o tempo limite existente.
def helpme(bot, update):
    chat_id = update.message.chat_id
    helpme_player = randomigo()             # Vamos escolher alguém pra zoar!
    bot.send_message(chat_id=chat_id, text="Lá vem você me amolar pedindo ajuda né? Oh well, como eu sou uma máquina "
                                           "desprovida de emoções, não faz diferença quantas vezes você chama esse "
                                           "comando. Vai da consciência de cada um"
                                           " (viu, " + helpme_player + ")? Pois bem:")
    helpme_player = randomigo()             # Mais um migo pra tirar onda.
    bot.send_message(chat_id=chat_id, text="/pintudo - Razão da minha existência. Vamos eleger um pintudo! \n"
                                           "/teste - Será que estou vivo? Descubra com esse comando. \n"
                                           "/getid - Quer descobrir seu chat ID por qualquer motivo? Fique à vontade, "
                                           "mas não me envolva em nada além disso! Já basta meu mestre ser amigo do "
                                           + helpme_player + ".\n"
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
        time_player = randomigo()  # Vamos escolher alguém pra zoar!
        timelimit_value, timelimit_message = get_timelimit()
        bot.send_message(chat_id=chat_id, text="Difícil você fazer alguma coisa certo, né? (eu estou olhando pra você, "
                                               + time_player + "? O limite se mantém em: " + str(timelimit_value) +
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


# Função que efetivamente para o bot, através de uma outra thread.
def stop(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="Vou nanar agora, boa noite!")
    threading.Thread(target=shutdown).start()
    print("Aviso: O bot está desligando...")


def shutdown():
    # Função de desligamento! É chamada pela stop para botar a mão na massa.
    global updater
    updater.stop()
    updater.is_idle = False


def messenger(bot_message):

    send_text = 'https://api.telegram.org/bot' + bot_token + \
                '/sendMessage?chat_id=' + kubinha_chatID + \
                '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)
    return response.json()


print("Funcionalidades Gerais OK")

# -------------------------------------------------------------------------------------------------
# ---------------------------------------------MAIN------------------------------------------------
# -------------------------------------------------------------------------------------------------


# Função principal, que conecta ao Telegram e realiza as transações.
def main():
    print("Inicialização dos comandos...")
    global updater
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('pintudo', shotcaller))       # >>> Habilitação da função pintudo no bot.
    dp.add_handler(CommandHandler('teste', teste))              # >>> Habilitação da função de teste no bot.
    dp.add_handler(CommandHandler('help', helpme))              # >>> Habilitação da função de ajuda no bot.
    dp.add_handler(CommandHandler('timelimit', timelimit))      # >>> Habilitação da função de tempo limite no bot.
    dp.add_handler(CommandHandler('getid', get_chat_id))        # >>> Habilitação da função de ID no bot.
    dp.add_handler(CommandHandler('stop', stop))        # >>> Habilitação da função de shutdown no bot.

    dp.add_handler(CommandHandler('changetime', timemanager, pass_args=True))       # >>> Habilitação da função de
    print("Comandos OK")                                                            # gestão de tempo no bot.
    updater.start_polling()
    print("Aviso: A varredura contínua por comandos foi iniciada; o bot está funcional.")
    updater.idle()
    print("Aviso: A execução do bot foi encerrada.")


if __name__ == '__main__':
    messenger("Olá, papai! Estou online! :D")
    main()


