from napalm import get_network_driver
driver = get_network_driver('ios')
device = driver('192.168.1.109', 'ccna', 'ccna')
device.open()

device.load_merge_candidate(filename='/home/kali/Desktop/test.cfg')
diff= device.compare_config()
if len(diff) == 0:
	device.discard_config()
	print("Nothing to change")
	print(diff)
else:
	device.commit_config()
	print("success")
	print(diff)

device.close()
