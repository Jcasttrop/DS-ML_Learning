import requests
import threading

def get_name():
    response = requests.get('https://randomuser.me/api/')
    if response.status_code == 200:
        results = response.json()['results']
        name = results[0]['name']['first']
        print(name)

if __name__ == '__main__':
    #Esto es secuencial, por lo cual para que se ejecute el siguiente proceso, 
    # debe terminar el anterior
    # for i in range(10):
    #     get_name()

    for i in range(10):
        #Esto es concurrente, por lo cual se ejecutan los procesos al mismo tiempo
        thread = threading.Thread(target=get_name) #traget es la funcion que se va a ejecutar
        thread.start() #si no se pone start, no se ejecuta el thread (porque el thread es programado para su ejecucion en el futuro)
        