#En python nosotros podemos crear varios threads por cada tarea que necesitemos

import threading

def exeutor_a():
    for x in range(10):
        print(f'Executor A, iteracion: {x}')

def exeutor_b():
    for x in range(10):
        print(f'Executor B, iteracion: {x}')

def exeutor_c():
    for x in range(10):
        print(f'Executor C, iteracion: {x}')

thread_A = threading.Thread(target=exeutor_a)
thread_B = threading.Thread(target=exeutor_b)
thread_C = threading.Thread(target=exeutor_c)

thread_A.start()
thread_B.start()
thread_C.start()

#La alternancia de los threads es aleatoria, por lo cual no se puede saber cual
#  va a ser el orden de ejecucion, porque depende de la maquina y del sistema operativo
#  y de como se maneje la memoria y los recursos 