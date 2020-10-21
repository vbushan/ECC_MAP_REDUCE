import rpyc

conn = rpyc.connect('35.227.100.231', 8080)
server = conn.root

print(server.add(1, 2))
