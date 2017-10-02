from sl_net import sl_net

net = sl_net()
net.wait_for_clients(3,5005)
print net.receive()
net.send("World")
net.close()
