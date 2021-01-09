from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('192.168.1.1', 'ccna', 'ccna')
iosvl2.open()

ios_output = iosvl2.get_interfaces_ip()
print (ios_output)
