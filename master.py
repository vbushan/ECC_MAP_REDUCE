import rpyc
from rpyc.utils.server import ThreadedServer
import datetime
import socket
import gcp_interface as cmp_eng
import traceback
from multiprocessing import Process


class Master(rpyc.Service):
    def __init__(self):
        super().__init__()
        self.cluster = dict()

    def on_connect(self, conn):

        time = datetime.datetime.now()
        print('Client Connected on ', time)

    def on_disconnect(self, conn):
        time = datetime.datetime.now()
        print('Client Disconnected on', time)

    def exposed_add(self, a, b):
        return a+b

    def exposed_init_cluster(self, num_mappers, num_reducers):

        # Create Total Workers parallely
        """
        spawn_processes = []
        for i in range(num_mappers):
            spawn_processes.append(
                Process(target=self.spawn_worker, args=('MAPPER', i+1)))

        for i in range(num_reducers):
            spawn_processes.append(
                Process(target=self.spawn_worker, args=('REDUCER', i+1)))

        """

        # Store mappers and reducers in a dictionary

        # Start KV Server

        # Generate a Cluster ID

        pass

    def spawn_worker(self, role, index):
        try:
            pass

        except Exception as e:
            traceback.print_exc()

    def spawn_kv(self):
        pass

    def exposed_run_mapred(self, a, b):

        # Read Input
        # Store Input in KV

        # Start Mapper execute
        # Stop Mappers

        # Start Reducer execute
        # Stop Reducers

        pass

    def exposed_destroy_cluster(self):

        # Delete mappers and reducers
        pass


if __name__ == "__main__":

    t = ThreadedServer(Master, hostname=socket.gethostbyname(
        socket.gethostname()), port=8080)

    t.start()
