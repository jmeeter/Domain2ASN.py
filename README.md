# Domain2ASN.py
Easily convert a domain name to ASN using Python.
# Requirements
You will need a Cloudflare account (free) since the first step of this script utilizes the Cloudflare domain intel API to retrieve the domain's IP address. Additionally you will need a ipinfo.io account (free) to utilize their IP lookup API to retrieve the IP's ASN.

# Usage

    python3 Domain2ASN.py <cloudflare_account_id> <cloudflare_auth_token> <domain>
