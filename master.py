import rpyc
from rpyc.utils.server import ThreadedServer
import socket

import datetime


class Master(rpyc.Service):
    def on_connect(self, conn):

        time = datetime.datetime.now()
        print(f'Client Connected on {time}')

    def on_disconnect(self, conn):
        time = datetime.datetime.now()
        print(f'Client Disconnected on {time}')

    def exposed_add(self, a, b):
        return a+b


t = ThreadedServer(Master, hostname=socket.gethostbyname(
    socket.gethostname()), port=8080)

t.start()
