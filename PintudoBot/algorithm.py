# Estudo de Python!

# Criado por Henrique Kubinhetz em 08/05/2019
# encoding: UTF-8
# Nome da aula: algorithm

# Algoritmo de teste!

import random


pintudos =\
{
    "1": "Henrique",
    "2": "Tuts",
    "3": "Gus",
    "4": "Key",
    "5": "Eriert",
    "6": "Nickolas",
    "7": "Chuco",
    "8": "Tony",
    "9": "Jardel",
    "10": "Jão",
    "11": "Werner"
}

pintudo_id = str(random.randint(1, 11))
print(pintudo_id)
print("Parabéns, " + pintudos[pintudo_id] + "! " + "Você é o pintudo do dia!")

