from socket import *
from multiprocessing import Process
from os import getpid

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM) 

def answer_client(connectionSocket, addr):
    print(f"Server Process {getpid()} established TCP connection with Client {addr}")
    while True:
        sentence = connectionSocket.recv(1024).decode() 
        capitalizedSentence = sentence.upper() 
        connectionSocket.send(capitalizedSentence.encode()) 

if __name__ == '__main__':
    serverSocket.bind(('', serverPort)) 
    serverSocket.listen(4)
    print('The server is ready to receive')
    while True:
        connectionSocket, addr = serverSocket.accept()
        p = Process(target=answer_client, args=(connectionSocket, addr))
        p.start()