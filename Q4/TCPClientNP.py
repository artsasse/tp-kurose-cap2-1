from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
while(True):
    N = input("Digite o valor de N: ")
    # Converte a string para int
    N = int(N)
    for i in range(N):
        # Converte para string e envia para o servidor
        i = str(i)
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName,serverPort)) 
        clientSocket.send(i.encode()) 
        clientSocket.close()