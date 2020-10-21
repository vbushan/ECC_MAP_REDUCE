import googleapiclient
import configparser
import gcp_interface as cmp_eng
import pprint
import traceback

config = configparser.ConfigParser()
config.read('config.ini')


startup_script = open(
    os.path.join(
        os.path.dirname(__file__), 'master-startup-script.sh'), 'r').read()

compute = googleapiclient.discovery.build('compute', 'v1')


project = config['MAP_REDUCE']['PROJECT_ID']
zone = config['MAP_REDUCE']['ZONE']
NAME = config['MASTER']['NAME']

try:

    create_op = create_instance(compute, project, zone,
                                'sample-master', startup_script)

    print('Creating Master instance....')

    status = wait_for_operation(compute, project, zone, create_op['name'])
    pprint(status)

    print('[Checkpoint] Master Instance Created')

except Exception as e:
    traceback.print_exc()
