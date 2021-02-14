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

tn.write(b"en\n")
tn.write(b"terminal length 0\n")
tn.write(b"sh run\n")
tn.write(b"exit\n")
file_wri=open("R1.txt","+w")
file_wri.write(tn.read_all().decode('ascii'))
file_wri.close()
