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

#INFORMANDO O SUCESSO DA CONEXÃO
print('Conectado em', ender)

#LAÇO PARA REPETIÇÃO
while True:
    
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
        

        


