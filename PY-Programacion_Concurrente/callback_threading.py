import requests
import threading
import logging

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def pokemon_name(response_json):
    name = response_json.get('forms')[0]['name']
    logging.info(f'El nombre del pokemon es {name}')

def user_name(response_json):
    name = response_json.get('results')[0]['name']['first']
    logging.info(f'El nombre del usuario es {name}')

def error_callback(response):
    logging.error(f'Error al hacer la peticion {response.status_code}')


def request(url, success_calbback, error_callback):
    response = requests.get(url)
    if response.status_code == 200:
        success_calbback(response.json) #convertimos el diccionario en json
    else:
        error_callback(response)


if __name__ == '__main__':
    thread_pokemon = threading.Thread(target=request, kwargs={
        'url': 'https://pokeapi.co/api/v2/pokemon/1/',
        'success_calbback': pokemon_name,
        'error_callback': error_callback
    })
    thread_pokemon.start()
    thread_user = threading.Thread(target=request, kwargs={
        'url': 'https://randomuser.me/api/',
        'success_calbback': user_name,
        'error_callback': error_callback
    })
 
 #con kwargs podemos pasarle los argumentos a la funcion que queremos ejecutar en el thread