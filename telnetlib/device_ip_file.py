import getpass
import telnetlib

user = input("Username: ")
password = getpass.getpass()

f = open ('device_ip')

for IP in f:
    IP=IP.strip()
    print ("Configuring Switch " + (IP))
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
       tn.read_until(b"Password: ")
       tn.write(password.encode('ascii') + b"\n")
    tn.write(b"conf t\n")
    tn.write(b"int loo 1\n")
    tn.write(b"ip addr 10.0.0.1 255.255.255.0\n")
    tn.write(b"int loo 2\n")
    tn.write(b"ip addr 20.0.0.1 255.255.255.0\n")
    tn.write(b"int loo 3\n")
    tn.write(b"ip addr 30.0.0.1 255.255.255.0\n")

    tn.write(b"end\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))
