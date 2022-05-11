from socket import *
serverName = 'localhost'
serverPort = 12006
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort)) 
while(True):
    message = input("Enviar: ")
    clientSocket.send(message.encode())
    response = clientSocket.recv(1024) 
    print(f'De ({serverName}, {serverPort}): {response.decode()}')
    # Procurei uma boa maneira de verificar se uma conexão TCP
    # está fechada, mas não achei nenhuma simples
    if "Obrigado" in response.decode():
        clientSocket.close()
        break