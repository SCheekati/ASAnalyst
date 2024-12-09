import requests
from config import RIPESTAT_API

def fetch_as_data(asn):
    data = {
        "asn_neighbors": fetch_ripe_data(f"https://stat.ripe.net/data/asn-neighbours/data.json?resource={asn}"),
        "whois_info": fetch_ripe_data(f"https://stat.ripe.net/data/whois/data.json?resource={asn}"),
        "routing_history": fetch_ripe_data(f"https://stat.ripe.net/data/bgplay/data.json?resource={asn}")
    }
    return data

def fetch_ripe_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data from {url}")
