import socket
import re

def is_valid(password):
    if len(password) < 6 or len(password) > 12:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[$#@]", password):
        return False
    return True

def start_server():
    HOST = '0.0.0.0'
    PORT = 8092

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)

    print("Server đang lắng nghe...")

    conn, addr = server.accept()
    print("Kết nối từ:", addr)

    data = conn.recv(1024).decode()
    print("Nhận:", data)

    passwords = data.split(",")

    valid_list = []
    for p in passwords:
        if is_valid(p.strip()):
            valid_list.append(p.strip())

    result = ",".join(valid_list)

    conn.send(result.encode())

    conn.close()
    server.close()