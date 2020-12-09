from netmiko import ConnectHandler

R1={
    'device_type': 'cisco_ios',
    'ip': '10.0.0.10',
    'username':'ccna',
    'password':'ccna'
    }

net_connect= ConnectHandler(**R1)
config_set=['hostname R1',
            'router ospf 1',
            'network 192.168.1.0 0.0.0.255']
output=net_connect.send_config_set(config_set)

print(output)
