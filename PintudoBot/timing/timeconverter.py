# Vamos programar em Python!

# Criado por Henrique Kubinhetz em 15/08/2019
# encoding: UTF-8
# Nome do arquivo: timeconverter

# Este código realiza simples cálculos para converter diferentes medidas de tempo em segundos.
# Sua utilização será feita pelo gettime.py, que dá margem para alterar o tempo limite de uma determinada contagem.


# Conversão de minutos para segundos:


def minutes2s(minutes):
    seconds = minutes * 60                              # >>> 60 segundos por minuto.
    return seconds

# Conversão de horas para segundos:


def hours2s(hours):
    seconds = hours * 60 * 60                           # >>> 60 minutos/hora * 60 segundos/minuto.
    return seconds

# Conversão de dias para segundos:


def days2s(days):
    seconds = days * 60 * 60 * 24                       # >>> 24 horas por dia.
    return seconds

# Conversão de semanas para segundos:


def weeks2s(weeks):
    seconds = weeks * 60 * 60 * 24 * 7                  # >>> 7 dias por semana.
    return seconds

# Conversão de tempo baseado na entrada:

def timeconverter(string):
    print(string[0])
    if string[0]== 'm'or string[0] == 'M':
        return minutes2s(int(string[1:]))
    elif string[0]== 'h'or string[0] == 'H':
        return hours2s(int(string[1:]))
    elif string[0]== 'd'or string[0] == 'D':
        return days2s(int(string[1:]))
    elif string[0]== 'w'or string[0] == 'W':
        return weeks2s(int(string[1:]))
    else:
        return int(string[1:])



