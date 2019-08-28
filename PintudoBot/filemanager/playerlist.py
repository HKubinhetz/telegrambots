# Vamos programar em Python!

# Criado por Henrique Kubinhetz em 30/07/2019
# encoding: UTF-8
# Nome do arquivo: playerlist

# Definição de um Dicionário Novo

pintudos =\
{
    "1": "@120938790 (Kubinha)",
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


def playerlist_write():
    # Definição de Função de Escrita

    playerlist_file = open("playerlist.txt", "w")
    playerlist_file.write(str(pintudos))
    playerlist_file.close()


# Definição da Função de Leitura e Conversão
def playerlist_read():

    # >>> Leitura:
    playerlist_file = open("playerlist.txt", "r+")
    playerlist_content = eval(playerlist_file.read())

    return playerlist_content

    # >>> Conversão:
    playerlist_dictionary = eval(playerlist_content)
    for i in playerlist_dictionary:
        print(playerlist_dictionary[i])                     # Print para mostrar que tá tudo funcionando:


