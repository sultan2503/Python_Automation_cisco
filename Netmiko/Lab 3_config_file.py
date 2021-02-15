from netmiko import ConnectHandler

R1={
    'device_type': 'cisco_ios',
    'ip': '192.168.1.10',
    'username':'ccna',
    'password':'ccna'
    }

net_connect= ConnectHandler(**R1)
f=open("conf.txt")
config_set=[]
for i in f:
    config_set.append(i.strip())
output=net_connect.send_config_set(config_set)

print(output)
