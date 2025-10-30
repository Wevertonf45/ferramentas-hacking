#Importações de bibliotecas
import socket
import pyfiglet

#Apresentação
texto = pyfiglet.figlet_format('Port Scanner, by Weverton', font='slant')
print(texto)


target_host = input('Enter a host to scan: ')
ports = [80, 443, 8080, 8443, 8000, 3000, 5000, 9000, 22, 21, 20, 25, 587, 465, 3306, 5432, 6379, 27017]


for port in ports:
    connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect.settimeout(1)
    
    code = connect.connect_ex((target_host, port))
    if code == 0:
        print('Port {} is open'.format(port))
    else:
        print('Port {} is closed'.format(port))
    connect.close()