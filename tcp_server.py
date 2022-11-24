# 소켓 프로그래밍에 필요한 API를 제공하는 모듈
import socket

ip = 'localhost'
port = 50001

#소켓 객체 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#소켓 주소 정보 할당
server_socket.bind((ip,port))

#연결 리스닝(동시 접속) 수 설정
server_socket.listen(10)

print("[클라이언트 연결 대기]")

#연결 수락(클라이언트 정보(소켓, 주소) 반환)
client_socket, address = server_socket.accept()
print("클라이언트 IP 주소 :", address[0])

#클라이언트로 받은 데이터 수신
data = client_socket.recv(1024).decode("UTF-8")
print("받은 메시지 :",data)

#클라이언트에게 데이터 전송
client_socket.send(data.encode("UTF-8"))

#소켓 닫기
client_socket.close()
server_socket.close()
print("[연결 종료]")
