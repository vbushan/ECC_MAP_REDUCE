import rpyc
from rpyc.utils.server import ThreadedServer
import datetime
import socket


class KV_Store(rpyc.Service):

    def __init__(self):
        pass

    def on_disconnect(self, conn):
        pass

    def on_connect(self, conn):
        pass
