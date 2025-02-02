from socket import *
#import socket

# 서버 소켓 생성
host = "127.0.0.1" # 자기자신 로컬 아이피
port = 55555 # 포트 번호 = 프로그램 식별번호

client_socket = socket(AF_INET, SOCK_STREAM) # 소켓 생성
client_socket.connect((host, port)) # 서버 주소와 서버 포트번호

print("연결 확인 완료")

client_socket.send("안녕하세요. 저는 클라이언트입니다.".encode("utf-8")) # 서버에게 데이터 전송

data =  client_socket.recv(1024) # 클라이언트가 보낸 데이터 수신

print('받은 데이터: ' + data.decode('utf-8'))

client_socket.close() # 서버 소켓 닫기 
