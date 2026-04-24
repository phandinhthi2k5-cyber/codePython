import socket

def start_client():
    HOST = '127.0.0.1'
    PORT = 8092

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    data = input("Nhập mật khẩu (cách nhau dấu ,): ")

    client.send(data.encode())

    result = client.recv(1024).decode()
    print("Mật khẩu hợp lệ:", result)

    client.close()