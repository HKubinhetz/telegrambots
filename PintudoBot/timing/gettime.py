# Estudo de Python!

# Criado por Henrique Kubinhetz em 11/05/2019
# encoding: UTF-8
# Nome da aula: gettime

# Esse código calcula quanto tempo se passou desde a última vez que o programa foi rodado.

# ONDE ESTAMOS:
# Falta converter a unidade de tempo (mexe em timelimit também! Um ninho de if talvez sirva, ou algo como um "switch"!)
# Falta colocar QUANDO o próximo sorteio será válido nas presentes circunstâncias! (essa vai ser foda kkk)
# Falta incorporar o módulo ao código principal.

# ---------- Imports ----------

import time


# ---------- Main Code ----------

def get_timelimit():
    # >>> Essa função muda o tempo limite que deve ser atingido pelo timer.

    timelimit_pointer = open("timelimit.txt", 'r+')     # Abre o arquivo e lê o tempo limite existente.
    timelimit = timelimit_pointer.read()

    timelimit_pointer.close()                           # Fecha a referência pois sou programador exemplo.

    return timelimit                                    # Retorna o tempo e a mensagem!


def changelimit(new_limit):
    # >>> Essa função muda o tempo limite que deve ser atingido pelo timer.

    timelimit_pointer = open("timelimit.txt", 'r+')     # Abre o arquivo e lê o tempo limite existente.
    timelimit = int(timelimit_pointer.read())

    # Se o novo tempo é válido, o mesmo é escrito. Do contrário, o anterior se mantém.
    if new_limit >= 0:
        timelimit_pointer.seek(0)                       # seek(0) muda o cursor do mouse para o inicio do arquivo
        timelimit_pointer.write(str(new_limit))
        timelimit_pointer.truncate()                    # truncate apaga quaisquer caracteres depois do novo número...
        timelimit_pointer.close()                       # ... como forma de evitar conflitos.
        return new_limit                                # devolve o timer e um true, pois deu certo!
    else:
        timelimit_pointer.close()
        return timelimit                                # devolve o timer e um false, pois deu ruim!


def gettime():
    # >>> Essa função consulta o tempo atual e o compara com o tempo inicial.
    # >>> Ela serve para posteriormente determinar se o tempo limite já foi atingido.

    try:
        # Abre o arquivo e lê o tempo limite.
        timelimit_pointer = open("timelimit.txt", 'r+')
        time_limit = int(timelimit_pointer.read())
        timelimit_pointer.close()

        # Abre o arquivo e lê o tempo original.
        timemanager_pointer = open("timemanager.txt", 'r+')
        original_time = float(timemanager_pointer.read())

        actual_time = time.time()                               # Retorna o tempo atual.

        timediff = actual_time - original_time                  # Calcula e retorna a diferença de tempo, em segundos.
        print("Tempo decorrido:" + str(timediff))

        # Tomada de Decisão:
        # Se a diferença de tempo já é maior que o tempo limite de tempo, um flag "True" é retornado e o tempo atual
        # sobrescreve o original, se tornando a referência para a próxima iteração.
        # Se o tempo limite ainda não foi atingido, nada acontece e um flag "False" é retornado.
        if timediff > time_limit:
            timediff_message = "Tempo Expirado!"

            timemanager_pointer.seek(0)
            timemanager_pointer.write(str(time.time()))
            timemanager_pointer.truncate()
            timemanager_pointer.close()

            return True, timediff_message

        else:
            remaining_time = format(time_limit - timediff,".1f")
            timediff_message = "O próximo pintudo do dia ainda não pode ser escolhido!" \
                               " Faltam " + str(remaining_time) + " segundos para o próximo sorteio válido." \
                               " Para verificar qual o tempo limite atual, digite /timelimit."
            timemanager_pointer.close()

            return False, timediff_message

    # Caso ocorra algum erro de valor, o código assume que o tempo limite foi atingido.
    except ValueError:
        print("Último valor perdido! Considerando que o tempo limite já passou...")

        return True

