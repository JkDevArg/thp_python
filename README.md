# Tool Hacking Plus

## Install

```bash
pip install -r requirements.txt
```

## Usage

```bash
████████╗██╗  ██╗██████╗
╚══██╔══╝██║  ██║██╔══██╗
   ██║   ███████║██████╔╝
   ██║   ██╔══██║██╔═══╝
   ██║   ██║  ██║██║
   ╚═╝   ╚═╝  ╚═╝╚═╝

usage: thp [-h] [-a] [-p PORT] [-t HOST] [-v] [-o OUTPUT]

THP CLI tool for network analysis

options:
  -h, --help            show this help message and exit
  -a, --about           Show help information
  -p PORT, --port PORT  Port number
  -t HOST, --host HOST  Host to analyze
  -v, --verbose         Enable verbose output
  -o OUTPUT, --output OUTPUT
                        Output file name
```

## Example

### simple scan

```bash
thp -t 127.0.0.1
```

### port scan

```bash
thp -p 80,22 -t 127.0.0.1
```

### debug mode

```bash
thp -p 80,22 -t 127.0.0.1 -v
```

### output file

```bash
thp -p 80,22 -t 127.0.0.1 -v -o output.txt
```
