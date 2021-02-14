#get username and password from user

import telnetlib

HOST = "192.168.1.10"
user = input("Enter your Username: ")
password = input("Enter Your Password: ")

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"sh ip int br\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
