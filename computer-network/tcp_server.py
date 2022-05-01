# Python TCP server

from socket import *

host = '127.0.0.1'
serverPort = 9999
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((host, serverPort))
serverSocket.listen(1)      # 1명만 상대한다는 의미
connectionSocket, addr = serverSocket.accept()  # 클라이언트가 전송한 내용을 받음
print('Connected by', addr)
case = connectionSocket.recv(4).decode()
connectionSocket.send("(Server)start writing words")

if case == "1": #Lower to Upper
    while True:
        data = connectionSocket.recv(1024).decode()
        if not data:
            break
        capitalize_data = data.upper()
        connectionSocket.send(capitalize_data.encode())
    
elif case == "2": #Upper to Lower
    while True:
        data = connectionSocket.recv(1024).decode()
        if not data:
            break
        capitalize_data = data.lower()
        connectionSocket.send(capitalize_data.encode())

else:
    while True:
        data = connectionSocket.recv(1024).decode()
        if not data:
            break
        sentence = "case is wrong..."
        connectionSocket.send(sentence.encode())
        connectionSocket.close()
        serverSocket.close()
connectionSocket.close()
serverSocket.close()