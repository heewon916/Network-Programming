# Python TCP server

from socket import *

user_list = {"Bob":"bob12!",
             "Alice":"alice34@",
             "Hamong":"ham92!",
             "Nodes":"node63!@"}

host = '127.0.0.1'
serverPort = 8080
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((host, serverPort))
serverSocket.listen(1)      # 1명만 상대한다는 의미
connectionSocket, addr = serverSocket.accept()  # 클라이언트가 전송한 내용을 받음
print('Connected by', addr)
print('\nthe server is ready to receive\n')

while True:
    connectionSocket, addr = serverSocket.accept()  # 클라이언트가 전송한 내용을 받음
    guest_info = connectionSocket.recv(1024).decode()
    id, pw = guest_info.split(' ')
    # 아이디가 이미 존재하는 경우
    if guest_info == "exit":
        print("(Server)Bye\n")
        break
    if id in user_list:
        sentence = "[!] You ALREADY joined\n"        
        connectionSocket.send(sentence.encode())
    # 아이디가 없는 경우: 회원가입을 진행 
    else:
        if pw.isalnum() or len(pw) <= 4 or pw.isalpha():
            sentence = "[!] FORMAT ERROR: 비밀번호는 영문자와 특수문자를 포함하여 4자리 이상이어야 합니다."
            continue
        else:
            user_list[id] = pw 
            sentence = f"Welcome! User {id}"
        connectionSocket.send(sentence.encode())    
connectionSocket.close()