import socket
from typing import Self

#nome da maquina e numero da porta

HOST = 'localhost'
PORT = 10000

#CRIANDO INVOCANDO O MÉTODO SOCKET

#AF INET(IPV4), STREAM POIS É TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen

#LAÇO PARA REPETIÇÃO
while True:
    
    #RECEBENDO DADOS DO CLIENTE, ACEITANDO A CONEXÃO
    print('Aguardando conexão')
    conn, addr = Self.accept()

    #RECEBENDO NÚMERO DO CLIENTE
    data = conn.recv(1024).decode()
    
#VERIFICANDO TAMANHO DO NÚMERO
if len(num) >10:
    
#GERANDO UMA STRING COM TAMANHO IGUAL AO NUMERO E MANDANDO DE VOLTA
    string = "a" * len(num)
    conn.send(string.encode())

#CASO NUMERO FOR MENOR DO QUE 10, VERIFICANDO SE ELE É PAR OU IMPAR        
else:
    if int(num) % 2 == 0:
        conn.send("PAR".encode())
    else:
        conn.send("ÍMPAR".encode())
        

#FECHANDOO A CONEXÃO
conn.close()      


