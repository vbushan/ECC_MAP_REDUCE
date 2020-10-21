import rpyc
from rpyc.utils.server import ThreadedServer
import socket


class Worker(rpyc.Service):
    def __init__(self):
        pass

    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass

    def exposed_execute(self, role, func, data, index):
        pass


if __name__ == "__main__":

    t = ThreadedServer(Master, hostname=socket.gethostbyname(
        socket.gethostname()), port=8080)

    t.start()
