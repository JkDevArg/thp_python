import json
import os
import socket
from thp.log import add_log

def load_services_json():
    with open(os.path.join(os.path.dirname(__file__), 'json/services.json'), 'r') as file:
        return json.load(file)

SERVICES_DATA = load_services_json()

def identify_service(port, log):
    port_str = str(port)
    if port_str in SERVICES_DATA:
        service_info = SERVICES_DATA[port_str][0]
        description = service_info["description"]
        types = []
        if service_info["tcp"]:
            types.append("TCP")
        if service_info["udp"]:
            types.append("UDP")
        return f"{description} ({', '.join(types)})"
    return "Unknown"

def analyze_services(ip, verbose, output, console_log):
    log = []
    services_info = []

    if verbose:
        add_log(log, f'Scanning services on {ip}...')
        add_log(console_log, f'Scanning services on {ip}...')

    for port in range(1, 1025):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex((ip, port))
            if result == 0:
                service = identify_service(port, log)
                services_info.append((port, service))

    if services_info:
        add_log(log, f'Services on {ip}: {services_info}')
        add_log(console_log, f'Services on {ip}: {services_info}')
    else:
        add_log(log, f'No services found on {ip}')
        add_log(console_log, f'No services found on {ip}')

    if output:
        add_log(log, f'Exporting log to {output}')

    return services_info
