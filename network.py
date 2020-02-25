import socket
import pickle


class Network:

    def __init__(self):

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "127.0.0.1"
        self.port = 5555
        self.addr = (self.server, self.port)

    def getP(self):

        return self.connect()

    def connect(self):
        """try:
            self.client.connect(self.addr)
            print("i'm here!!")
            return self.client.recv(2048).decode()
        except:
            print("i'm in except!!!")
            pass"""

        self.client.connect(self.addr)

        con = self.client.recv(2048).decode()

        con2 = int(con)
        return con2

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048 * 2))
        except socket.error as e:
            print(e)
