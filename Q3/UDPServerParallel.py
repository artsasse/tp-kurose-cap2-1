from socket import *
from multiprocessing import Process
from os import getpid

def answer_client(message, clientAddress, serverSocket):
    modifiedMessage = message.decode().upper() 
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    print(f"Process {getpid()} sent message to Client {clientAddress}")
    return

if __name__ == '__main__':
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_DGRAM) 
    serverSocket.bind(('', serverPort)) 
    while True:
        print("The server is ready to receive")
        message, clientAddress = serverSocket.recvfrom(2048)
        p = Process(target=answer_client, args=(message, clientAddress, serverSocket))
        p.start()

