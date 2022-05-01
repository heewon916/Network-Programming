# Python TCP Client

from socket import *

host = '127.0.0.1'
serverPort = 9999
clientSocket = socket(AF_INET, SOCK_STREAM)     # SOCK_STREAM: TCP 프로토콜을 사용한다는 의미
clientSocket.connect((host, serverPort))
print("Program for Lower to Upper and otherwise")
case = str(input("[!] What case do you need?\n\t(1)Lower to Upper (2)Upper to Lower (1/2)\n\t>>"))
clientSocket.send(case.encode())

while True:    
    sentence = str(input('Input :: '))
    if not sentence:
        print("(Client)Failed to write data\n")
        break
    if sentence == "exit":
        print("(Client)bye\n")
        break
    clientSocket.send(sentence.encode())
    print("(Client)send data ::", sentence)
    modifiedSentence = clientSocket.recv(1024)
    print("(Client)recieve data :: ", modifiedSentence.decode())
    
clientSocket.close()