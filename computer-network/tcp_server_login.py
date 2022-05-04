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
print('\nthe server is ready to receive\n')
connectionSocket, addr = serverSocket.accept()  # 클라이언트가 전송한 내용을 받음

while True:
    guest_info = connectionSocket.recv(1024).decode()
    id, pw = guest_info.split(' ')
    # 아이디가 이미 존재하는 경우
    if guest_info == "exit":
        print("(Server)Bye\n")
        break
    if id in user_list and pw == user_list[id]:
        sentence = "[!] You ALREADY joined\n"        
        connectionSocket.send(sentence.encode())
    # 아이디가 없는 경우: 회원가입을 진행 
    else:
        #print("pw = ", type(pw))
        if len(pw)<4 or pw.isdecimal():
            sentence = "[!] FORMAT ERROR: length should be longer than 4 and include alphabets with numbers\n"
        else:
            user_list[id] = pw 
            sentence = "(Server)Welcome!"
        connectionSocket.send(sentence.encode())    
connectionSocket.close()
serverSocket.close()