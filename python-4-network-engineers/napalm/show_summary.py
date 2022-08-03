from napalm import get_network_driver
#Here we specify which driver we're going to use
# at https://napalm.readthedocs.io/en/latest/support/ we can see the names of the drivers
driver = get_network_driver('ios')
iosvl2 = driver('192.168.122.72', 'andres', 'cisco')
iosvl2.open()

ios_output = iosvl2.get_facts()
print (ios_output)
