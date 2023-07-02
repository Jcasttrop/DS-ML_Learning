import logging

#Debug, info, warning, error, critical

logging.basicConfig(
    level=logging.DEBUG #muestra todos los mensajes de nivel 10 o superior
) #basicConfig es una funcion que configura el logging

def mensajes():
    logging.debug("Mensaje de debug")
    logging.info("Mensaje de info")
    logging.warning("Mensaje de warning")
    logging.error("Mensaje de error")
    logging.critical("Mensaje de critical")

if __name__ == '__main__':
    mensajes()