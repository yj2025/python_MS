# 서버 코드
import threading, socket

class ChatServer:

    #class 변수 / static 변수
    ip='localhost'  #or 본인 ip or 127.0.0.1
    port = 5555

    def __init__(self):
        self.server_soc = None      #서버 소켓(대문)
        self.client_soc = None      #클라이언트와 1:1 통신 소켓

    def open(self):
        self.server_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_soc.bind((ChatServer.ip, ChatServer.port))
        self.server_soc.listen()

    def sendMsg(self):#키보드 입력받아 상대방에게 메시지 전송.
        while True:
            msg = input('msg:')
            data = msg.encode(encoding='utf-8')
            self.client_soc.sendall(data)
            #if msg ==  '/stop':
            #    break

    def recvMsg(self):#상대방이 보낸 메시지 읽어서 화면에 출력
        while True:
            data = self.client_soc.recv(1024)
            msg = data.decode()
            print('상대방 메시지:', msg)
            #if msg ==  '/stop':
            #    break

    def run(self):
        self.open()
        self.client_soc, addr = self.server_soc.accept()#클라이언트 1명만 받음
        print(addr, '접속함')
        
        th1 = threading.Thread(target=self.sendMsg)
        th1.start()

        th2 = threading.Thread(target=self.recvMsg)
        th2.start()

    def close(self):
        self.client_soc.close()
        self.server_soc.close()

def main():
    server = ChatServer()
    server.run()

main()