import socket

class GoogleConnector:
    def __init__(self):
        self.target_host = 'www.google.com'
        self.target_port = 80
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.client_socket.connect((self.target_host, self.target_port))
        self.client_socket.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
        response = self.client_socket.recv(4096)
        print(response.decode())

    def close(self):
        self.client_socket.close()


