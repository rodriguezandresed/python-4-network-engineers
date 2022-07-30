import getpass
import telnetlib

HOST = "192.168.122.72"
user = input("Enter your telnet user ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
#Still need to hide password
tn.write(b"cisco\n")
tn.write(b"conf t\n")
# tn.write(b"vlan 2\n")
# tn.write(b"name Python_VLAN_2\n")
#ofc you can use a loop 
for n in range (2,11):
    # b"\n" means send an "enter"
    tn.write(b"vlan " +str(n).encode('ascii') + b"\n")
    tn.write(b"name Python_VLAN_" +str(n).encode('ascii') + b"\n")
tn.write(b"end\n")
tn.write(b"wr\n")
tn.write(b"exit\n")


print(tn.read_all().decode('ascii'))