# pastRecon 🦝

Passive fuzzing tool that uses the Wayback Machine to retrieve archived URLs for a given domain. Useful for discovering hidden or outdated endpoints during reconnaissance and bug bounty hunting.

## Features

- Passive URL discovery via the Wayback Machine
- Supports file extension filtering (e.g., `.php`, `.txt`)
- Lightweight and easy to use
- Requires only Python 3 and `requests`

## Installation

Clone the repository and make sure you have `requests` installed:

```bash
git clone https://github.com/abund4nt/pastRecon.git
cd pastRecon
pip install requests
````

## Usage

```bash
python3 pastRecon.py -u <target-domain> [-f <extension>]
```

### Examples:

```bash
python3 pastRecon.py -u example.com
python3 pastRecon.py -u example.com -f php
```

## Arguments

| Flag             | Description                                                 |
| ---------------- | ----------------------------------------------------------- |
| `-u`, `--url`    | Target domain to scan (e.g., example.com)                   |
| `-f`, `--filter` | (Optional) Filter results by extension (e.g., php, js, txt) |
| `-h`, `--help`   | Show help message                                           |

