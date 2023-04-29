import socket

#nome da maquina e numero da porta

HOST = 'localhost'
PORT = 10000

#CRIANDO INVOCANDO O MÉTODO SOCKET

#AF INET(IPV4), STREAM POIS É TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen

#RECEBENDO DADOS DO CLIENTE, ACEITANDO A CONEXÃO
print('Aguardando conexão')
conn, ender = s.accept()