from socket import *
from getpass import getpass
serverName = 'localhost'
serverPort = 12005
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort)) 
while(True):
    username = input("Digite o seu nome de usuário: ")
    password = getpass("Digite a sua senha: ")
    clientSocket.send(username.encode()) 
    clientSocket.send(password.encode()) 
    response = clientSocket.recv(1024) 
    print(f'From ({serverName}, {serverPort}): {response.decode()}')