#import socket module
import socket

#function to get ip address
def get_ip_address(url):
    return socket.gethostbyname(url)

#main function
def main():
    host = input("Enter the host name: ")
    print(get_ip_address(host))
if __name__ == "__main__":
    main()
    print(get_ip_address())
if __name__ == "__main__":
    main()  