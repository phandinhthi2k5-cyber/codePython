import socket

def start_server():
    HOST = '0.0.0.0'
    PORT = 9999

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)

    print("Server đang lắng nghe...")

    conn, addr = server.accept()
    print("Kết nối từ:", addr)

    data = conn.recv(1024).decode()
    print("Nhận:", data)

    a, b = map(int, data.split())
    tong = a + b

    conn.send(str(tong).encode())

    conn.close()
    server.close()