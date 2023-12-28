import time
import json
import socket

class PortWatch:
    def __init__(self) -> None:        
        self.closed = []
        self.open = []
        self.blacklist = []
        self.host = socket.gethostbyname(socket.gethostname())

        for port in range(65535):
            try:
                serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                serv.bind((self.host,port))
                self.closed.append(port)
            except:
                self.open.append(port)
            serv.close()
        
        self.port_info = {
            "open":self.open,
            "closed":self.closed,
            "blacklist":self.blacklist,
            "host":self.host
        }

    def portInfo(self, key):
        return self.port_info[key]

    def listen(self, port):
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(("localhost", port))
            msg = client_socket.recv(1024)
            print(f"recieved: {msg.decode('utf-8')}")

        except Exception as e:
            print(f"Error: {e}")

portwatch = PortWatch()

while True:
    portwatch.listen(5500)