# Python-Port-Scanner

This project is a simple port scanner written in Python as part of my networking and cybersecurity practice.  
It performs a basic TCP connect scan over a user-defined port range and reports which ports respond as open.  
The goal of this version was to understand how socket connections work and how a scanner handles timeouts, errors, and loop-based scanning.

The script prompts for:
- a target host (IP address or domain)
- a starting port
- an ending port

It attempts to connect to each port once, prints any that are open, and provides a brief summary at the end, including total scan time.

Example output:

    Scanning scanme.nmap.org from port 20 to 90...

    Port 22 is OPEN
    Port 80 is OPEN

    Scan complete in 0.52 seconds.
    Open ports found: 22, 80

Key areas I focused on while building this:
- working with Python’s socket library
- handling connection attempts and timeouts cleanly
- iterating through port ranges efficiently
- tracking scan duration
- structuring small security tools in a clear and readable way

Planned improvements for a future version:
- multithreading to improve scan speed
- basic service/banner detection
- command-line argument support
- optional output to file

This tool is intended for educational use only. Please scan only systems you are authorized to test.