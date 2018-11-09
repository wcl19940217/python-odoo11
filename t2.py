# socket tcp服务器端编程
import socket
import threading


class ChatServer:
    def __init__(self, ip='127.0.0.1', port=9000):
        self.socket = socket.socket()
        self.ipaddr = (ip, port)

    def start(self):
        self.socket.bind(self.ipaddr)
        self.socket.listen()
        threading.Thread(target=self.accept).start()

    def accept(self):
        sock, client = self.socket.accept()
        print(sock, client)
        threading.Thread(target=self.recv, args=(sock, client)).start()

    def recv(self, sock, client):
        while True:
            data = sock.recv(1024)
            sock.send(data)

    def stop(self):
        self.socket.close()


def main():
    cs = ChatServer()
    cs.start()


if __name__ == '__main__':
    main()

2、  # tcp客户端编程
import socket
import threading


class ChatClient:
    def __init__(self, ip='127.0.0.1', port=9000):
        self.client = socket.socket()
        self.ipaddr = (ip, port)

    def start(self):
        self.client.connect(self.ipaddr)
        self.client.send(b'hello')
        threading.Thread(target=self.recv).start()

    def recv(self):
        data = self.client.recv(1024)
        print(data)

    def send(self, data):
        data = data.encode()
        self.client.send(data)

    def stop(self):
        self.client.close()


def main():
    cc = ChatClient()
    cc.start()
    while True:
        cmd = input('>>>')
        if cmd.strip() == 'quit':
            cc.stop()
            break
        cc.send(cmd)


if __name__ == '__main__':
    main()
