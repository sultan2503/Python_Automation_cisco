from napalm import get_network_driver
driver = get_network_driver('eos')
device = driver('192.168.1.109', 'ccna', 'ccna')
device.open()

device.load_replace_candidate(filename='/home/kali/Desktop/test.conf')
diff= device.compare_config()
if diff == 0:
	device.discard_config()
	print("Nothing to change")
else:
	device.commit_config()
	print("success")

device.close()
