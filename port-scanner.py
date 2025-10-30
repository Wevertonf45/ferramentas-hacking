import socket

target_host = input('Enter a host to scan: ')


for port in range(1, 65536):
    connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect.settimeout(1)
    
    code = connect.connect_ex((target_host, port))
    if code == 0:
        print('Port {} is open'.format(port))
    else:
        print('Port {} is closed'.format(port))
    connect.close()