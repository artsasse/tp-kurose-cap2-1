from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM) 
serverSocket.bind(('', serverPort)) 
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()
    print(f"Connection established with: {addr}")
    while True: # Suporta apenas 1 conexão ativa
        number = connectionSocket.recv(1024).decode() 
        print(f"Client says: {number}")