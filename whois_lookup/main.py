import socket  # Import socket module for network communication

def whois_lookup(domain: str):  # Performs a WHOIS lookup for a given domain
    s = socket.socket(socket.AF_INET,  # Create a TCP socket
    socket.SOCK_STREAM)                 
    s.connect(("whois.markmonitor.com", 43))   # Connect to the WHOIS server
    s.send((domain + "\r\n").encode())  # Send the domain name to the server
    response = s.recv(4096).decode()  # Receive the response from the server
    s.close()
    return response

print(whois_lookup("amazon.com"))  # Performs a WHOIS lookup for "amazon.com"
