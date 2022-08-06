from netmiko import ConnectHandler

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.72',
    'username': 'andres',
    'password': 'cisco'
}
#Connects to the Switch on iosv_12
net_connect = ConnectHandler(**iosv_l2)
#Sends a command to the switch
output = net_connect.send_command('show ip int brief')
print (output)
#creates a list of configuration commands
config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print (output)

for n in range (2,21):
    print ("Creating VLAN " + str(n))
    config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print (output) 
