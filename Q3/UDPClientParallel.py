from socket import *
from multiprocessing import Pool
from os import getpid

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

def askServer(message):
    clientSocket.sendto(message.encode(),(serverName, serverPort)) 
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048) 
    print(f"Processo {getpid()} recebeu: {modifiedMessage.decode()}")
    # print(f"Server Address: {serverAddress}")

if __name__ == '__main__':
    messages = ["a", "b", "c", "d"]
    with Pool(processes=4) as pool:
        pool.map(askServer, messages)
    
    
# clientSocket.close()
