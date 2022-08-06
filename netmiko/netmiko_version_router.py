from netmiko import ConnectHandler

net_connect = ConnecHandler(**ios_router)
output = net_connect.send_command('show version')

output1 = output1.find('1941')

if output1 > 0
	C1941 = True
else
	C1941 = False

router = True

if router
	if c1941:
		print ( 'This is a 1941 router')
	else:
		print ('This is a router but not a 1941 router)
else:
	print ('Not a router')
