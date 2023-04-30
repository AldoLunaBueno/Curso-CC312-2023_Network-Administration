import pprint
from netmiko import ConnectHandler

connection_info = {
    'device_type': 'cisco_ios',
    'host': '192.168.56.105',
    'port': 22,
    'username': 'cisco',
    'password': 'cisco123!'
}

with ConnectHandler(**connection_info) as conn:
    out = conn.send_command("show running-config")
    print(out)