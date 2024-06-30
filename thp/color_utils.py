from colorama import Fore, Style

def colored_text(text, color):
    return f'{color}{text}{Style.RESET_ALL}'

def yellow_text(text):
    return colored_text(text, Fore.YELLOW)

def red_text(text):
    return colored_text(text, Fore.RED)

def cyan_text(text):
    return colored_text(text, Fore.CYAN)
