import socket

def start_client():
    HOST = '127.0.0.1'
    PORT = 9999

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    a = input("Nhập a: ")
    b = input("Nhập b: ")

    client.send(f"{a} {b}".encode())

    result = client.recv(1024).decode()
    print("Tổng từ server:", result)

    client.close()