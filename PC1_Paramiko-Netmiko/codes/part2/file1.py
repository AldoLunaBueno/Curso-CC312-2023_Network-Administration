from netmiko import ConnectHandler

"""
connection_info = {
    'device_type': 'cisco_ios',
    'host': 'sandbox-iosxe-recomm-1.cisco.com',
    'port': 22,
    'username': 'developer',
    'password': 'C1sco12345'
} 
"""

connection_info = {
    'device_type': 'cisco_ios',
    'host': '192.168.56.105',
    'port': 22,
    'username': 'cisco',
    'password': 'cisco123!'
}


with ConnectHandler(**connection_info) as conn:
    print("Succesfully connected!")
    
