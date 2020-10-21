import googleapiclient.discovery
from test import create_instance, delete_instance, wait_for_operation, list_instances, get_ip
import rpyc
from pprint import pprint
import os

startup_script = open(
    os.path.join(
        os.path.dirname(__file__), 'master-startup-script.sh'), 'r').read()

compute = googleapiclient.discovery.build('compute', 'v1')
project = 'vathepalli-vamsi-bushan-293105'
zone = 'us-east1-b'


create = create_instance(compute, project, zone,
                         'sample-master', startup_script)

print('\n\n')

print('Waiting for instance to create')
status = wait_for_operation(compute, project, zone, create['name'])
pprint(status)
print('Done Waiting')

print('Created Instace IP')

IP = get_ip(compute, project, zone, 'sample-master')
print('Instance Internal IP Address- ', IP)

with open('master-ip.txt', 'w') as file:
    file.write(IP)


"""

rpyc.core.protocol.DEFAULT_CONFIG['sync_request_timeout'] = None

master = rpyc.connect(ext_ip, port=8080,
                      config=rpyc.core.protocol.DEFAULT_CONFIG).root

print('Result from VM', master.add(1, 2))


print('\n\n')


delete = delete_instance(compute, project, zone, 'sample-instance-python')
print('Waiting for instance to delete')
status = wait_for_operation(compute, project, zone, delete['name'])
pprint(status)
print('Done Waiting')


"""
