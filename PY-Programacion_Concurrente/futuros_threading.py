import logging
import threading
import time
import requests
from concurrent.futures import Future


def show_pokemon_name(future):
    response = future.result()
    if response.status_code != 200:
        response_json = response.json()
        pokemon_name = response_json.get('forms')[0]['name']
        logging.info(f'El nombre del pokemon es: {pokemon_name}')


def generate_request(url):
    future = Future()

    thread = threading.Thread(target=(
        lambda: future.set_result(requests.get(url).content)) 
        )
    
    thread.start()

    return future

if __name__ == '__main__':
    future = generate_request('https://pokeapi.co/api/v2/pokemon/1')
    future.add_done_callback(show_pokemon_name)

    while not future.done():
        logging.info('Esperando respuesta del servidor...') #Aqui el thread principal puede hacer otra cosa

        time.sleep(1)
    else:
        logging.info('Terminamos la ejecucion del programa')