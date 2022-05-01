# Python TCP Client

from socket import *

serverName = '127.0.0.1'
serverPort = 8080
clientSocket = socket(AF_INET, SOCK_STREAM)     # SOCK_STREAM: TCP 프로토콜을 사용한다는 의미
clientSocket.connect((serverName, serverPort))

sentence = str(input('Input LowerCase sentence: '))
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print("From server: ", modifiedSentence.decode())
clientSocket.close()