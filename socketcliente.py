import socket

# Setando Host e Porta
Host = 'localhost'
Port = 10000

# Criar um objeto socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar o socket à porta onde o servidor está escutando
server_address = (Host, Port)
sock.connect(server_address)

# Gerando um numero inteiro aleatorio com ate 30 digitos
num = random.randint(1, 999999999999999999999999999999)  

# Enviando o numero gerado para o servidor
sock.sendall(str(num).encode())

# Recebendo a resposta do servidor
data = sock.recv(1024)
Resp = data.decode() + "FIM"

# Imprimindo a resposta do servidor
print(Resp)

# Devolvendo a resposta do servidor
sock.sendall(Resp.encode())

# Fechando a conexão
sock.close()