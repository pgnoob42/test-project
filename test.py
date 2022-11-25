# 소켓 프로그래밍에 필요한 API 제공
import socket
import threading #스레드(Thread) 모듈

ip = '192.168.0.232'
port = 50001

#데이터 수신 함수


def receive(client_socket):
    state = True

    while True:
        #예외 처리
        try:
            #메시지 수신
            message = client_socket.recv(1024).decode("UTF-8")

            #메시지 출력
            if state:
                print(message, end="")
                state = False
            else:
                print(message)
                
        except Exception as error:
            print("[에러 발생]", error)
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    #서버와 연결
    client_socket.connect((ip, port))

    #서브 스레드 객체 생성
    thread = threading.Thread(target=receive, args=(client_socket,))
    thread.daemon = True #스레드를 생성한 메인 스레드가 종료되면 같이 종료
    thread.start() #스레드 시작

    while True:
        #서버로 메시지 전송
        message = input().encode("UTF-8")
        client_socket.send(message)

        # '/exit' 메시지 전송할 경우 퇴장
        if message == "/exit":
            break


