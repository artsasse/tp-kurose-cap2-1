from socket import *
serverName = 'localhost'
serverPort = 12001
clientSocket = socket(AF_INET, SOCK_DGRAM)
while True:
    N = input("Digite o valor de N: ")
    # Converte a string para int
    N = int(N)
    for i in range(N):
        # Converte para string e envia para o servidor
        i = str(i)
        clientSocket.sendto(i.encode(),(serverName, serverPort)) 
    
# clientSocket.close()