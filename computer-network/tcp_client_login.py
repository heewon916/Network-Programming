# Python TCP Client

from socket import *

host = '127.0.0.1'
serverPort = 8080
clientSocket = socket(AF_INET, SOCK_STREAM)     # SOCK_STREAM: TCP 프로토콜을 사용한다는 의미
clientSocket.connect((host, serverPort))

print("Program for Login...")
print("Usage: to quit >> write 'exit'")
print("***Start Login***\n")
while True:
    id = str(input('Input ID: '))
    pw = str(input('Input PW: '))

    clientSocket.send((id+' ' +pw).encode())
    modifiedSentence = clientSocket.recv(1024)
    print("From server: ", modifiedSentence.decode())    
    
    keep_on_state = str(input("\tKeep on State?(y/n) >>"))
    if keep_on_state == 'n':
        clientSocket.send("exit".encode())
        break
print("(Client)Bye\n")
clientSocket.close()