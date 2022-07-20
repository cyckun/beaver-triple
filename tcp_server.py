 
import threading
import socket


class TcpServer:

    def __init__(self):
        self.ip = '127.0.0.1'
        self.port = 9851
        self.tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server.bind((self.ip, self.port))

    def listenPort(self):
        self.tcp_server.listen(5)
        print("Server> listen port...")
        self.con, address = self.tcp_server.accept()
        print(f"Server> 已与{address}建立连接")

    def sendMessage(self, message):
        if self.con is None:
            print("Server> 未连接到客户端")
        else:
            self.con.send(message.encode(encoding='utf-8'))

    def getMessage(self):
        flag = True
        if self.con is None:
            print("Server> 未与客户端连接")
        while flag:
            recv_data = str(self.con.recv(1024), encoding="utf-8")
            if recv_data == 'exit':
                self.con.close()
                flag = False
            else:
                print(f"\nClient> {recv_data}\nServer> ")

    def closeServer(self):
        self.con.close()
        self.tcp_server.close()
