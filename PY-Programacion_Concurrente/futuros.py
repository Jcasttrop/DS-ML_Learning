import threading
import logging
import time
from concurrent.futures import Future


def callback_future(future):
    logging.info('Hola soy un callback que se ejecuta cuando el futuro posee un valor')
    logging.info(f'El valor del futuro es: {future.result()}') #obtenemos el valor del futuro
    #podemos registrar la n cantidad de callbacks que queramos al futuro


if __name__ == '__main__':
    future = Future() #aqi le damos el futuro
    future.add_done_callback(callback_future) #le asignamos el callback

    logging.info('Comenzamos una tarea compleja')
    time.sleep(2)
    logging.info('Terminamos la tarea compleja')

    #asiganandole un valor al futuro
    future.set_result('El resultado de la tarea compleja') #recibe cualquier objeto

    #Aqui el futuro ya posee un valor; y es donde se activa el callback