# Python TCP Client

from socket import *

serverName = '127.0.0.1'
serverPort = 8080
clientSocket = socket(AF_INET, SOCK_STREAM)     # SOCK_STREAM: TCP 프로토콜을 사용한다는 의미
clientSocket.connect((serverName, serverPort))

print("***Start Login***")
id = str(input('Input ID: '))
pw = str(input('Input PW: '))

clientSocket.send((id+' ' +pw).encode())
modifiedSentence = clientSocket.recv(1024)
print("From server: ", modifiedSentence.decode())
clientSocket.close()