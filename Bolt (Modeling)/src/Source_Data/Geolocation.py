import http.client
import json

def get_ip_info():
    conn = http.client.HTTPSConnection("ipinfo.io")
    conn.request("GET", "/json")
    res = conn.getresponse()
    ip_info = json.loads(res.read().decode())
    ip = ip_info["ip"]
    city = ip_info["city"]
    region = ip_info["region"]
    country = ip_info["country"]
    loc = ip_info["loc"]
    org = ip_info["org"]
    warning = ":WARNING EMOJI:" if "VPN" in org else ""
    return f"{warning} IP_INFO\n" \
           f"IP:        {ip}\n" \
           f"City:      {city}\n" \
           f"Region:    {region}\n" \
           f"Country:   {country}\n" \
           f"GPS:       {loc}\n" \
           f"Organization: {org}\n"
