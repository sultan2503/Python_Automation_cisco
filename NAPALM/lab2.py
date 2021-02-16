from napalm import get_network_driver
driver = get_network_driver('ios')
device = driver('192.168.1.109', 'ccna', 'ccna')
device.open()

device.load_replace_candidate(filename='/home/kali/Desktop/test.conf')
device.commit_config()
device.close()
