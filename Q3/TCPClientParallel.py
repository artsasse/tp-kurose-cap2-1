from socket import *
from multiprocessing import Pool
from os import getpid
import time

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

def askServer(sentence):
    # Por algum motivo não consegue estabelecer uma conexão
    clientSocket.connect((serverName,serverPort)) 
    clientSocket.send(sentence.encode()) 
    modifiedSentence = clientSocket.recv(1024) 
    print(f"Processo {getpid()} recebeu: {modifiedMessage.decode()}")

if __name__ == '__main__':
    sentences = ["a", "b", "c", "d"]
    with Pool(processes=4) as pool:
        for i in range(4):
            pool.map(askServer, sentences)
            time.sleep(2)
    
    
