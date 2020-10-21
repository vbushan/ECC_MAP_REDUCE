import googleapiclient.discovery
from test import create_instance, delete_instance, wait_for_operation, list_instances, get_ip
import rpyc
from pprint import pprint


startup_script = open(
    os.path.join(
        os.path.dirname(__file__), 'worker-startup-script.sh'), 'r').read()

compute = googleapiclient.discovery.build('compute', 'v1')
project = 'vathepalli-vamsi-bushan-293105'
zone = 'us-east1-b'


create = create_instance(compute, project, zone, 'sample-worker')

print('\n\n')

print('Waiting for instance to create')
status = wait_for_operation(compute, project, zone, create['name'])
pprint(status)
print('Done Waiting')

print('Created Instace IP')

IP = get_ip(compute, project, zone, 'sample-master')
print('Instance Internal IP Address- ', IP)

with open('worker-ip.txt', 'w') as file:
    file.write(IP)
