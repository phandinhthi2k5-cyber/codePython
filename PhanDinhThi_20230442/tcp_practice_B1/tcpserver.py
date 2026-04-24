import socket

def start_server():
    HOST = '0.0.0.0'
    PORT = 8090

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)

    print("Server đang lắng nghe...")

    conn, addr = server.accept()
    print("Kết nối từ:", addr)

    data = conn.recv(1024).decode()
    print("Client gửi:", data)

    conn.send("From SERVER TCP".encode())

    conn.close()
    server.close()