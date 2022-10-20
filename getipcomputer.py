import os
import socket

def get_ip_address():
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Connect to google DNS server
    s.connect(("8.8.8.8", 80))
    # Get the IP address of the local machine
    return s.getsockname()[0]

def main():
    print(get_ip_address())

if __name__ == "__main__":
    main()