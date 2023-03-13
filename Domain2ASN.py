import sys
import requests

def get_domain_ip(account_id, domain, auth_token):
    url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/intel/domain?domain={domain}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_token}"
    }
    response = requests.get(url, headers=headers)
    if response.ok:
        domain_intel = response.json()
        ipv4_addresses = [r['value'] for r in domain_intel['result']['resolves_to_refs'] if r['id'].startswith('ipv4-addr')]
        if ipv4_addresses:
            return ipv4_addresses[0]
        else:
            return None
    else:
        response.raise_for_status()

def get_ip_asn(ip):
    url = f"https://ipinfo.io/{ip}/org?token=<YOUR_TOKEN>"
    response = requests.get(url)
    if response.ok:
        return response.text.strip()
    else:
        response.raise_for_status()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 Domain2ASN.py <account_id> <auth_token> <domain>")
        sys.exit(1)

    account_id = sys.argv[1]
    auth_token = sys.argv[2]
    domain = sys.argv[3]

    ip_address = get_domain_ip(account_id, domain, auth_token)

    if ip_address:
        asn = get_ip_asn(ip_address)
        print(f"ASN for {ip_address}: {asn}")
    else:
        print(f"No IPV4 addresses found for {domain}")
