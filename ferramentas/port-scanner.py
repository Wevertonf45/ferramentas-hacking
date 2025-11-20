#Importações de bibliotecas
import socket
import pyfiglet


#Apresentação
texto = pyfiglet.figlet_format('Port Scanner', font='slant')
print("*" * 100)
print(texto)
print("*" * 100)
print("\n")

#Criar as funcões
def scann_completo():
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

def scann_curto():
	target_host = input('Enter a host do scan: ')
	ports = [80, 443, 8080, 8443, 3000, 5000, 8000, 8888, 9080, 9443, 3306, 5432, 1521, 1433, 27017, 6379, 9200, 11211, 27018, 27019, 25, 465, 587, 110, 995, 143, 993, 22, 21, 20, 989, 990, 23, 3389, 5900, 5985, 5986, 161, 162, 137, 138, 139, 445, 1883, 8883, 15672, 5672, 9092, 2181, 2375, 2376, 6443, 10250, 53, 123, 67, 68, 179, 5601, 8081, 9090, 9100, 10000, 3001, 5173, 5174]

	for port in ports:
		connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		connect.settimeout(1)
		code = connect.connect_ex((target_host, port))

		if code == 0:
			print('Port {} is open'.format(port))
		else:
			print('Port {} is closed'.format(port))

		connect.close()


#Iniciar o scanner
print('Informe 1 para fazer o scann das 65.565 portas')
print('Informe 2 para fazer o scann das principais portas')

escolha = int(input('Escolha um número: '))

if escolha == 1:
	scann_completo()
elif escolha == 2:
	scann_curto()
else:
	print('Escolha uma opção válida!')
