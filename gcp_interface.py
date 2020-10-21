import googleapiclient.discovery
import os
import time


def list_instances(project, zone):
    compute = googleapiclient.discovery.build('compute', 'v1')

    result = compute.instances().list(project=project, zone=zone).execute()
    return result['items'] if 'items' in result else None


def create_instance(project, zone, name, startup_script):
    # Get the latest Debian Jessie image.
    compute = googleapiclient.discovery.build('compute', 'v1')

    image_response = compute.images().getFromFamily(
        project='debian-cloud', family='debian-9').execute()

    source_disk_image = image_response['selfLink']

    # Configure the machine
    machine_type = "zones/%s/machineTypes/n1-standard-1" % zone

    config = {
        'name': name,
        'machineType': machine_type,

        # Specify the boot disk and the image to use as a source.
        'disks': [
            {
                'boot': True,
                'autoDelete': True,
                'initializeParams': {
                    'sourceImage': source_disk_image,
                }
            }
        ],

        # Specify a network interface with NAT to access the public
        # internet.
        'networkInterfaces': [{
            'network': 'global/networks/default',
            'accessConfigs': [
                {'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}
            ]
        }],

        # Allow the instance to access cloud storage and logging.
        'serviceAccounts': [{
            'email': 'default',
            'scopes': [
                'https://www.googleapis.com/auth/devstorage.read_write',
                'https://www.googleapis.com/auth/logging.write',
                'https://www.googleapis.com/auth/cloud-platform'
            ]
        }],


        'metadata': {
            'items': [{
                # Startup script is automatically executed by the
                # instance upon startup.
                'key': 'startup-script',
                'value': startup_script
            }]
        }

    }

    return compute.instances().insert(
        project=project,
        zone=zone,
        body=config).execute()


def wait_for_operation(project, zone, operation):
    compute = googleapiclient.discovery.build('compute', 'v1')

    print('Waiting for operation to finish...')
    while True:
        result = compute.zoneOperations().get(
            project=project,
            zone=zone,
            operation=operation).execute()

        if result['status'] == 'DONE':
            print("done.")
            if 'error' in result:
                raise Exception(result['error'])
            return result

        time.sleep(1)


def delete_instance(project, zone, name):
    compute = googleapiclient.discovery.build('compute', 'v1')

    return compute.instances().delete(
        project=project,
        zone=zone,
        instance=name).execute()


def get_ip(project, zone, name):
    compute = googleapiclient.discovery.build('compute', 'v1')

    instance = compute.instances().get(
        project=project, zone=zone, instance=name).execute()

    internal_ip = instance['networkInterfaces'][0]['networkIP']
    #ext_ip = instance['networkInterfaces'][0]['accessConfigs'][0]['natIP']

    return internal_ip


"""
compute = googleapiclient.discovery.build('compute', 'v1')
project = 'vathepalli-vamsi-bushan-293105'
zone = 'us-east1-b'


#print(create_instance(compute, project, zone, 'sample-instance-python'))


#print(list_instances(compute, project, zone))

print(delete_instance(compute, project, zone, 'sample-instance'))
print(delete_instance(compute, project, zone, 'sample-instance-python'))
"""
