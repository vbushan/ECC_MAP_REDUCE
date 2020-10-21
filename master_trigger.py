import googleapiclient
import configparser
import gcp_interface as cmp_eng
import pprint
import traceback
from multiprocessing import Process
import worker_functions

config = configparser.ConfigParser()
config.read('config.ini')


startup_script = open(
    os.path.join(
        os.path.dirname(__file__), 'master-startup-script.sh'), 'r').read()


PROJECT = config['MAP_REDUCE']['PROJECT_ID']
ZONE = config['MAP_REDUCE']['ZONE']
NAME = config['MASTER']['NAME']
NUM_MAPPERS = config['MASTER']['NUM_MAPPERS']
NUM_REDUCERS = config['MASTER']['NUM_REDUCERS']
# INPUT_LOCATION =

try:

    create_op = cmp_eng.create_instance(PROJECT, ZONE,
                                        NAME, startup_script)

    print('Creating Master instance....')

    status = wait_for_operation(project, zone, create_op['name'])
    pprint(status)

    print('[Checkpoint] Master Instance Created')

    MASTER_IP = cmp_eng.get_ip(PROJECT, ZONE, NAME)
    MASTER_PORT = int(config['MAP_REDUCE']['PORT'])

    print('MASTER NODE ADDRESS', (MASTER_IP, MASTER_PORT))

    #conn = rpyc.connect(MASTER_IP, MASTER_PORT)

    #master_node = conn.root

    #master_node.init_cluster(NUM_MAPPERS, NUM_REDUCERS)

    # master_node.map_reduce()


except Exception as e:
    traceback.print_exc()
