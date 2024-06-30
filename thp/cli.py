import argparse
from colorama import init, Fore, Style
from thp import network, services

init()

logo = """
████████╗██╗  ██╗██████╗
╚══██╔══╝██║  ██║██╔══██╗
   ██║   ███████║██████╔╝
   ██║   ██╔══██║██╔═══╝
   ██║   ██║  ██║██║
   ╚═╝   ╚═╝  ╚═╝╚═╝
"""

def print_logo():
    print(Fore.GREEN + logo + Style.RESET_ALL)

def print_about():
    print(Fore.CYAN + 'THP CLI Tool # Created by Joaquin Centurion \nGithub: https://github.com/JkDevArg/thp_python' + Style.RESET_ALL)
    print(Fore.MAGENTA + ' \n\nUsage: thp [-a] [-p PORT] [-t HOST] [-s] [-k PACKETS]' + Style.RESET_ALL)

def parse_args():
    parser = argparse.ArgumentParser(description='THP CLI tool for network analysis')
    parser.add_argument('-a', '--about', action='store_true', help='Show help information')
    parser.add_argument('-p', '--port', type=int, help='Port number')
    parser.add_argument('-t', '--host', type=str, help='Host to analyze')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')
    parser.add_argument('-o', '--output', type=str, help='Output file name')
    parser.add_argument('-s', '--services', action='store_true', help='Scan for services on the host')
    parser.add_argument('-k', '--packets', type=int, choices=range(1, 6), help='Number of packets to send per second (1-5)')

    return parser.parse_args()

def main():
    print_logo()
    args = parse_args()
    console_log = []

    if args.about:
        print_about()
    elif args.host:
        if args.verbose:
            print(Fore.YELLOW + f'Analyzing host: {args.host} with verbose mode enabled' + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + f'Analyzing host: {args.host}' + Style.RESET_ALL)
        network.analyze_host(args.host, args.verbose, args.output, args.packets)
        if args.services:
            services.analyze_services(args.host, args.verbose, args.output, console_log)
    elif args.port:
        print(Fore.GREEN + f'Port specified: {args.port}' + Style.RESET_ALL)
    else:
        print(Fore.RED + 'Error: No host or port specified. Use -h for help.' + Style.RESET_ALL)

if __name__ == '__main__':
    main()
