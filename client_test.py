from sl_net import sl_net

net = sl_net()

net.connect_as_client('localhost',5005)
net.send("hello")
print net.receive()
net.close()
