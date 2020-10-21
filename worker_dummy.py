

import rpyc


rpyc.core.protocol.DEFAULT_CONFIG['sync_request_timeout'] = None


#SERVER = open(master-ip.txt, 'w').read()

SERVER = '10.142.0.24'

conn = rpyc.connect(SERVER, 8080,
                    config=rpyc.core.protocol.DEFAULT_CONFIG)
server = conn.root

print('Response from Master', server.add(1, 2))


"""
SERVER = '127.0.0.1'
PORT = 8080

rpyc.core.protocol.DEFAULT_CONFIG['sync_request_timeout'] = None

conn = rpyc.connect(SERVER, PORT,
                    config=rpyc.core.protocol.DEFAULT_CONFIG)
server = conn.root


"""
"""
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
"""
