import socket


#SETEANDO PORTA E HOST
HOST ='localhost'
PORT = 10000

#AF INET(IPV4), STREAM POIS É TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

#LAÇO PARA REPETIÇÃO
while True: 
    #RECEBENDO DADOS DO CLIENTE, ACEITANDO A CONEXÃO
    print('Aguardando conexão')
    conn, ender = server_socket.accept()

    #INFORMANDO O SUCESSO DA CONEXÃO
    print('Conectado em', ender)
    #RECEBENDO NÚMERO DO CLIENTE
    num = conn.recv(1024).decode()
    
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


