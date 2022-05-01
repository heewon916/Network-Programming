# Python UDP Server
from socket import *
serverPort = 8080
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))         # 소켓과 AF를 연결하는 과정; 앞부분은 ip, 뒷부분은 포트로 (ip, port) 형식
# ''는 INADDR_ANY를 의미한다고 합니다. 즉, 모든 인터페이스와 연결하고 싶다면 빈 문자열을 넣으면 된다
# serverSocket.listen(1)                      # 상대방의 접속을 기다리는 단계로 넘어가겠단 의미
#connectionSock, addr = serverSocket.accept()
#print(str(addr),'에서 접속이 확인되었습니다.')
print("The server is ready to recieve")

while True:
    message, clientAddress = serverSocket.recvfrom(1024)
    modifiedMessage = message.decode().lower()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)