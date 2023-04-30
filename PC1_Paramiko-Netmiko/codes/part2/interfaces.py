from netmiko import ConnectHandler
import pprint

connection_info = {
    'device_type': 'cisco_ios',
    'host': '192.168.56.105',
    'port': 22,
    'username': 'cisco',
    'password': 'cisco123!'
}

with ConnectHandler(**connection_info) as conn:
    out = conn.send_command("show interfaces", use_genie=True)
    pprint.pprint(out)
    # pprint.pprint(out['GigabitEthernet1']['bandwidth']) # 1000000
    for interface in out.keys():
        print(interface)