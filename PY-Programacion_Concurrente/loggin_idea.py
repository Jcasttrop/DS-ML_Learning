#Con loggin podemos hacer muchas cositas curiosas a la hora de buscar los "logs" de nuestro 
#programa, desde hacer que se guarden, darles un formato, que muestre la funcion 
#que genera el error, la linea, etc.

import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s: %(levelname)s [%(filename)s:%(funcName)s:%(lineno)s] %(message)s',
    filename='logs.txt'
)

#asi podemos enviar un correo con el error


def send_email(subject, message, sender_email, receiver_email, smtp_server, smtp_port, smtp_username, smtp_password):
    # Crear el mensaje de correo electrónico
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # Establecer la conexión con el servidor SMTP
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Enviar el correo electrónico
        server.send_message(msg)

# Ejemplo de uso
try:
    # Código que puede generar un error
    1 / 0
except Exception as e:
    # Registrar el error
    logging.error(str(e))
    
    # Enviar el correo con el log
    subject = "Error en la aplicación"
    message = str(e)
    sender_email = "tucorreo@gmail.com"  # Dirección de correo electrónico del remitente
    receiver_email = "destinatario@gmail.com"  # Dirección de correo electrónico del destinatario
    smtp_server = "smtp.gmail.com"  # Servidor SMTP (por ejemplo, para Gmail)
    smtp_port = 587  # Puerto SMTP (por ejemplo, para Gmail)
    smtp_username = "tucorreo@gmail.com"  # Nombre de usuario SMTP
    smtp_password = "tuc0ntr4s3ñ4"  # Contraseña SMTP

    send_email(subject, message, sender_email, receiver_email, smtp_server, smtp_port, smtp_username, smtp_password)