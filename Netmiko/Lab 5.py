
from netmiko import ConnectHandler
host=['192.168.1.10','192.168.1.11']
for i in host:
    R1 = {
        'device_type': 'cisco_ios',
        'ip': i,
        'username': 'ccna',
        'password': 'ccna'
    }

    net_connect = ConnectHandler(**R1)
    output = net_connect.send_command('sh ip int br')
    f=open(i,"+w")
    f.write(output)
    print (output)
