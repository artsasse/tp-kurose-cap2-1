from socket import *

# Inicia o servidor
serverPort = 12005
serverSocket = socket(AF_INET,SOCK_STREAM) 
serverSocket.bind(('', serverPort)) 
serverSocket.listen(1)

# Simulação das credenciais guardadas no servidor
user1_username = "aluno"
user1_password = "senha"

# Verifica as credenciais
print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()
    print(f"Connection established with: {addr}")
    while True: # Suporta apenas 1 conexão ativa
        username = connectionSocket.recv(1024).decode()
        password = connectionSocket.recv(1024).decode() 

        if username == user1_username and password == user1_password:
            success = "Você está logado agora!"
            connectionSocket.send(success.encode())
        else:
            error = "Erro no nome de usuário ou senha"
            connectionSocket.send(error.encode())