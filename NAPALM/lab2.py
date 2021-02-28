from napalm import get_network_driver
driver = get_network_driver('ios')
device = driver('192.168.1.109', 'ccna', 'ccna', optional_args={'global_delay_factor': 2})
device.open()

device.load_merge_candidate(filename='/home/kali/Desktop/test.cfg')
device.commit_config()
device.close()
