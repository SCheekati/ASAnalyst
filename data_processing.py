import json
import re

def process_as_data(data):
    structured_data = {}
    structured_data['asn_neighbors'] = extract_asn_neighbors(data['asn_neighbors'])
    structured_data['whois_info'] = extract_whois_info(data['whois_info'])
    structured_data['routing_history'] = extract_routing_history(data['routing_history'])
    return structured_data

def extract_asn_neighbors(raw_data):
    return raw_data.get("data", {}).get("neighbours", [])

def extract_whois_info(raw_data):
    return raw_data.get("data", {}).get("records", [])

def extract_routing_history(raw_data):
    return raw_data.get("data", {}).get("events", [])
