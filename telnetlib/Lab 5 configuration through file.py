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

f=open("conf.txt","+r")
for i in f:
    tn.write(b" "+i.encode('ascii').strip()+b"\n")

tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
