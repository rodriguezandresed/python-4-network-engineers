from netmiko import ConnectHandler

def netmiko_connection(ip, password):
        return {
        'device_type': 'cisco_ios',
        'ip':ip,
        'username': 'david',
        'password': password,
        }


list = ['192.168.122.72',
    '192.168.122.73',
    '192.168.122.74',
    '192.168.122.75',
    '192.168.122.76',
    '192.168.122.77',
    '192.168.122.78',
    '192.168.122.79',
    '192.168.122.80',
    '192.168.122.82',
    '192.168.122.84',
    ]
    

for ip_address in list:
    iosv = netmiko_connection(ip = ip_address, password = 'cisco')
    print(iosv)
    print ('Connecting to ' + ip)
    net_connect = ConnectHandler(**iosv)
    output = net_connect.send_command('show ip int brief')
    print(output)