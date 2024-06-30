import socket
import subprocess
from thp.log import add_log, export_log
from thp.color_utils import yellow_text, red_text, cyan_text

def analyze_host(host, verbose=False, output=None):
    log = []
    console_log = []

    try:
        if verbose:
            add_log(log, f'Resolving IP address for {host}...')
            add_log(console_log, f'Resolving IP address for {host}...')
        ip_address = socket.gethostbyname(host)
        add_log(log, f'IP address of {host}: {ip_address}')
        add_log(console_log, f'IP address of {host}: {ip_address}')

        if verbose:
            add_log(log, f'Pinging {host} to check if it is up...')
            add_log(console_log, f'Pinging {host} to check if it is up...')
        response = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
        if response.returncode == 0:
            add_log(log, f'{host} is up!')
            add_log(console_log, f'{host} is up!')
            if verbose:
                add_log(log, f'Ping output:\n{response.stdout}')
                add_log(console_log, f'Ping output:\n{response.stdout}')
            determine_os(ip_address, verbose, log, console_log)
            scan_ports(ip_address, verbose, log, console_log)
        else:
            add_log(log, f'{host} is down!')
            add_log(console_log, f'{yellow_text(host)} is {red_text("down")}!')
            if verbose:
                add_log(log, f'Ping output:\n{response.stdout}')
                add_log(console_log, f'Ping output:\n{response.stdout}')

    except socket.gaierror as e:
        add_log(log, f'Error resolving host: {e}')
        add_log(console_log, f'Error resolving host: {e}')

    if output:
        export_log(log, output)

    for line in console_log:
        print(cyan_text(line))

def determine_os(ip, verbose, log, console_log):
    try:
        if verbose:
            add_log(log, f'Determining OS for {ip}...')
            add_log(console_log, f'Determining OS for {ip}...')
        result = subprocess.run(['ping', '-c', '1', ip], capture_output=True, text=True)
        if 'ttl=64' in result.stdout.lower():
            add_log(log, f'{ip} is likely a Linux/Unix system')
            add_log(console_log, f'{ip} is likely a Linux/Unix system')
        elif 'ttl=128' in result.stdout.lower():
            add_log(log, f'{ip} is likely a Windows system')
            add_log(console_log, f'{ip} is likely a Windows system')
        else:
            add_log(log, f'Could not determine the OS of {ip}')
            add_log(console_log, f'Could not determine the OS of {ip}')
        if verbose:
            add_log(log, f'OS determination output:\n{result.stdout}')
            add_log(console_log, f'OS determination output:\n{result.stdout}')
    except Exception as e:
        add_log(log, f'Error determining OS: {e}')
        add_log(console_log, f'Error determining OS: {e}')

def scan_ports(ip, verbose, log, console_log):
    if verbose:
        add_log(log, f'Scanning ports on {ip}...')
        add_log(console_log, f'Scanning ports on {ip}...')
    open_ports = []
    for port in range(1, 1025):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)

    if open_ports:
        add_log(log, f'Open ports on {ip}: {open_ports}')
        add_log(console_log, f'Open ports on {ip}: {open_ports}')
    else:
        add_log(log, f'No open ports found on {ip}')
        add_log(console_log, f'No open ports found on {ip}')

    if verbose and open_ports:
        add_log(log, f'Open ports details: {open_ports}')
        add_log(console_log, f'Open ports details: {open_ports}')
