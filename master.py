import rpyc
from rpyc.utils.server import ThreadedServer
import configparser
import datetime
import socket
import gcp_interface as cmp_eng
import traceback
from multiprocessing import Process
from worker_trigger import start_worker_instance
import os
import concurrent.futures
import random

config = configparser.ConfigParser()
config.read('config.ini')


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

        self.num_mappers = int(config['MASTER']['NUM_MAPPERS'])
        self.num_reducers = int(config['MASTER']['NUM_REDUCERS'])

        # Create All Workers parallelly

        with concurrent.futures.ProcessPoolExecutor() as executor:
            mapper_names = [config['MAPPER']['NAME'] +
                            str(i) for i in range(1, self.num_mappers+1)]

            mappers = executor.map(self.spawn_worker, mapper_names)

            reducer_names = [config['REDUCER']['NAME'] +
                             str(i) for i in range(1, self.num_reducers+1)]

            reducers = executor.map(self.spawn_worker, reducer_names)

        self.cluster['ID'] = random.randint(1, 1000)
        self.cluster['MAPPERS'] = list(mappers)
        self.cluster['REDUCERS'] = list(reducers)

        # Start KV Server

    def spawn_worker(self, worker_name):
        try:

            return (worker_name, start_worker_instance(worker_name))

        except Exception as e:
            traceback.print_exc()

    def spawn_kv(self):
        pass

    def exposed_run_mapred(self, in_loc, map_func, red_func, out_loc):

        input_chunks = [[] for i in range(self.num_mappers)]

        # Read Input
        if os.path.isdir(in_loc):
            index = 0
            for file in os.listdir(in_loc):
                input_chunks[index] = open(os.path.join(
                    './books', file), 'r', encoding='utf-8').read()
                index += 1

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

    # t = ThreadedServer(Master, hostname=socket.gethostbyname(
    #    socket.gethostname()), port=8080)

    t = ThreadServer(Master, hostname='0.0.0.0', port=8080)
    t.start()
