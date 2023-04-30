from paramiko.client import SSHClient, AutoAddPolicy
import getpass

# Credentials for local CSR100v VM
# SSH_USER = "cisco"
# SSH_PASSWORD = "cisco123!"
# SSH_HOST = "192.168.56.105"
# SSH_PORT = 22

# Credentials for local CSR100v VM with input() and getpass
# SSH_USER = input("Username: ") # "cisco"
# SSH_PASSWORD = getpass.getpass("Password: ") # "cisco123!"
# SSH_HOST = input("IP host: ") # "192.168.56.105"
# SSH_PORT = 22 # Change this if your SSH port is different

# Credentials here are for a always-on Sandbox from Cisco DevNet
SSH_USER = "developer"
SSH_PASSWORD = "lastorangerestoreball8876"
SSH_HOST = "sandbox-iosxe-recomm-1.cisco.com"
SSH_PORT = "22" # Change this if your SSH port is different

client = SSHClient()
client.set_missing_host_key_policy(AutoAddPolicy())
client.load_system_host_keys()

try:
    client.connect(SSH_HOST, port=SSH_PORT,
                             username=SSH_USER,
                             password=SSH_PASSWORD,
                             look_for_keys=False)
    print("Connected succesfully!")
except Exception as e:
    print(f"Failed to establish connection: {e}")
finally:
    client.close()