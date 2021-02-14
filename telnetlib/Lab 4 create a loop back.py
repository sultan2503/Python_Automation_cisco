#Create a loopback

import getpass
import telnetlib

HOST = "192.168.1.10"
user = input("Enter your Username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"sh ip int br\n")
tn.write(b"conf t\n")
tn.write(b"int vlan 100\n")
tn.write(b"ip addr 1.1.1.1 255.255.255.255\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
