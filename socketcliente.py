import socket

# Setando Host e Porta
Host = 'localhost'
Port = 10000

# Criar um objeto socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)