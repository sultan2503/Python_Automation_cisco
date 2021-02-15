from netmiko import ConnectHandler

R1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.10',
    'username': 'ccna',
    'password': 'ccna'
}

net_connect = ConnectHandler(**R1)
output = net_connect.send_command('show ip int brief')
R1=open("R1_net.txt","+w")
R1.write(output)
R1.close()
