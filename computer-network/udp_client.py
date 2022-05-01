from http import server
from socket import *

serverName = '127.0.0.1'
serverPort = 8080 
clientSocket = socket(AF_INET, SOCK_DGRAM)      # AF(어드레스 패밀리)는 주소 체계에 해당한다. AF_INET은 IPv4를, AF_INET6는 IPv6를 의미한다
message = str(input("Input Lowercase sentence:"))
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
