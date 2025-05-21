#!/usr/bin/env python3

import argparse
import requests
import sys

def get_wayback_urls(domain, extension=None):
    print(f"[+] Starting passive scanning on: {domain}\n")

    url = f"https://web.archive.org/cdx/search/cdx?url=*.{domain}/*&output=json&fl=original&collapse=urlkey"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"[!] Error fetching data from Wayback Machine: {e}")
        sys.exit(1)

    data = response.json()
    
    if len(data) <= 1:
        print("[!] No data found.")
        return

    results = data[1:]  # skip header
    for entry in results:
        path = entry[0]
        if extension:
            if path.endswith(f".{extension}"):
                print(path)
        else:
            print(path)

    print(f"\n[+] Scanning {domain} completed.\n")

def main():
    parser = argparse.ArgumentParser(
        description="Passive endpoint discovery using the Wayback Machine"
    )
    parser.add_argument(
        "-u", "--url",
        help="Target domain/URL to scan (e.g., example.com)",
        required=True
    )
    parser.add_argument(
        "-f", "--filter",
        help="Filter results by file extension (e.g., php, txt, js)",
        default=None
    )

    args = parser.parse_args()

    get_wayback_urls(args.url, args.filter)

if __name__ == "__main__":
    main()

