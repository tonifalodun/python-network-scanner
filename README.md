# Python Network Scanner & Monitoring Tool

A Python-based network monitoring application that scans multiple network targets, determines whether each device is reachable using ICMP ping requests, and records the results in log and JSON files.

## Features

- Scans multiple network targets
- Determines whether devices are UP, DOWN, or TIMEOUT
- Generates timestamped log files
- Exports scan results to JSON
- Uses object-oriented programming and a modular architecture
- Supports both Windows and Unix-based operating systems

## Technologies Used

- Python
- Object-Oriented Programming (OOP)
- JSON
- File I/O
- Logging
- Exception Handling
- Subprocess
- Networking (ICMP Ping)

## Project Structure

```
network-scanner/
│
├── main.py
├── core/
├── network/
├── data/
├── logs/
└── output/
```

## How It Works

1. Reads a list of target devices from `targets.txt`.
2. Executes an ICMP ping request for each target.
3. Determines whether each target is UP, DOWN, or TIMEOUT.
4. Records timestamped scan results in a log file.
5. Exports the results as a structured JSON report.

## Example Output

```json
[
  {
    "name": "server01",
    "status": "DOWN",
    "timestamp": "2026-05-16T12:57:46.816195"
  },
  {
    "name": "server02",
    "status": "DOWN",
    "timestamp": "2026-05-16T12:57:46.816220"
  }
]
```

## Future Improvements

- Graphical user interface (GUI)
- Scan summary statistics
- User-defined target lists
- Additional network diagnostics
