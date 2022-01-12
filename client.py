import socket
import time


PORT = 4000
SERVER = "  linode ip address"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

def connect(): 
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client

def send(client, msg):
    message = msg.encode(FORMAT)
    client.send(message)

 

def start(): 
    answer = input('Would you like to connect (y/n) ? ')
    if answer.lower() != 'y':
        return

    connection = connect()
    while True:
        msg = input('Message (q for quit): ')

        if msg == 'q': 
            break

        send(connection, msg)

    send(connection, DISCONNECT_MESSAGE)
    time.sleep(1)
    print('Disconnected! ')

start()