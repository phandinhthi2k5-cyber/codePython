import threading
import time
import tcpserver
import tcpclient

def run_server():
    tcpserver.start_server()

def run_client():
    time.sleep(1)  
    tcpclient.start_client()

if __name__ == "__main__":
    t1 = threading.Thread(target=run_server)
    t2 = threading.Thread(target=run_client)

    t1.start()
    t2.start()

    t1.join()
    t2.join()