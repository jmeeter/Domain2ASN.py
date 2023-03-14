import sys
import socket
import requests
import re

# Get the domain name from command line argument
domain_name = sys.argv[1]

# Get the IP address for the domain name
ip_address = socket.gethostbyname(domain_name)
print("IP address for", domain_name + ":", ip_address)

# Use IPinfo.io to get the ASN for the IP address
url = f"https://ipinfo.io/{ip_address}/json"
response = requests.get(url)
data = response.json()
org = data["org"]
asn = re.search(r'\d+', org).group()
print("ASN for", ip_address + ":", asn)
