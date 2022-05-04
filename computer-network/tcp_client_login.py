# Python TCP Client

from socket import *

host = '127.0.0.1'
serverPort = 8080
clientSocket = socket(AF_INET, SOCK_STREAM)     # SOCK_STREAM: TCP 프로토콜을 사용한다는 의미
clientSocket.connect((host, serverPort))

print("Program for Login...")
print("Usage: to quit >> write 'exit' on ID")
while True:
    id = str(input('Input ID: '))
    pw = str(input('Input PW: '))

    if id == 'exit':
        clientSocket.send("exit exit".encode())
        break
    clientSocket.send((id+' ' +pw).encode())
    response = clientSocket.recv(1024)
    print(response.decode())
        

print("(Client)Bye\n")
clientSocket.close()