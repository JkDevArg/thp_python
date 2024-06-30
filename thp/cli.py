import argparse
from colorama import init, Fore, Style
from thp import network

init()

logo = """
████████╗██╗  ██╗██████╗
╚══██╔══╝██║  ██║██╔══██╗
   ██║   ███████║██████╔╝
   ██║   ██╔══██║██╔═══╝
   ██║   ██║  ██║██║
   ╚═╝   ╚═╝  ╚═╝╚═╝
"""

def main():
    print(Fore.GREEN + logo + Style.RESET_ALL)

    parser = argparse.ArgumentParser(description='THP CLI tool for network analysis')
    parser.add_argument('-a', '--about', action='store_true', help='Show help information')
    parser.add_argument('-p', '--port', type=int, help='Port number')
    parser.add_argument('-t', '--host', type=str, help='Host to analyze')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')
    parser.add_argument('-o', '--output', type=str, help='Output file name')

    args = parser.parse_args()

    if args.about:
        print(Fore.CYAN + 'THP CLI Tool # Created by Joaquin Centurion \nGithub: https://github.com/JkDevArg/thp_python'+ Style.RESET_ALL)
        print(Fore.MAGENTA + ' \n\nUsage: thp [-a] [-p PORT] [-t HOST]' + Style.RESET_ALL)
    elif args.host:
        if args.verbose:
            print(Fore.YELLOW + f'Analyzing host: {args.host} with verbose mode enabled' + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + f'Analyzing host: {args.host}' + Style.RESET_ALL)
        network.analyze_host(args.host, args.verbose, args.output)
    elif args.port:
        print(Fore.GREEN + f'Port specified: {args.port}' + Style.RESET_ALL)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()