from paramiko.client import SSHClient
from paramiko import SSHConfig

SSH_CONFIG = "config_file"
SSH_HOST = "192.168.56.105"

config = SSHConfig()
config_file = open(SSH_CONFIG)

config.parse(config_file)

dev_config = config.lookup(SSH_HOST)
client = SSHClient()
client.load_system_host_keys()

HOST = dev_config['hostname']
print(dev_config)
client.connect(HOST, port=int(dev_config['port']),
                     username=dev_config['user'],
                     password=dev_config['password'])
client.close()