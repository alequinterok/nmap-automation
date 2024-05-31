#!/usr/bin/env python3

import argparse
import os

class CustomHelpFormatter(argparse.HelpFormatter):    
    def format_help(self):
        help_str = super().format_help()
        return help_str.replace("show this help message and exit", "Show this help message and exit")


def open_file(file_path: str):
    try:
        with open(file_path, mode="r") as f:
            for ip in f:
                ip = ip.strip()  # Eliminar espacios en blanco alrededor de la dirección IP
                os.system(f"nmap -Pn --open {ip} -oN {ip}.nmap")
    except FileNotFoundError:
        print("Error. The file couldn't be opened")


def main():
    parser = argparse.ArgumentParser(description='Scan IP addresses from a file using Nmap.', formatter_class=CustomHelpFormatter)
    parser.add_argument('-f', '--file', help='Path to the file containing IP addresses. Each IP address should be on a separate line.')
    args = parser.parse_args()

    if args.file:
        file_path = args.file
        open_file(file_path)
    else:
        parser.print_usage()


if __name__ == "__main__":
    main()