# Python TCP server

from socket import *

serverPort = 8080
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)      # 1명만 상대한다는 의미

print('the server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()  # 클라이언트가 전송한 내용을 받음
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    #connectionSocket.close()