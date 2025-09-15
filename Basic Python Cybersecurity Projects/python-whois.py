import socket #Give python basic knowladge of http, https, what is important, domain

print("Enter a domain to perform a WHOIS lookup (e.g., example.com):")
example_site = input().strip() 


# Function to perform a WHOIS lookup  
def whois_lookup(domain: str): # Pass the WHOIS lookup in to a stream line argument called domain
    s = socket.socket(socket.AF_INET, #Basically stands for address family, internet 
    socket.SOCK_STREAM)  #Basically declaring if want a TCP socket type 
    s.connect(("whois.iana.org", 43)) #Collect the input and connect to the whois server on port 43
    s.send(f"{domain}\r\n".encode()) #Send the domain name to the whois server
    response = s.recv(4096).decode() #Recieve the response from the whois server (4096 - decodes to string so easy to read)
    s.close() 
    return response

print(whois_lookup(example_site)) 