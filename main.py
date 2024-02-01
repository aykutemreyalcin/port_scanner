import socket
def scan_port(ip_address,port):
    try:
        sock = socket.socket()
        sock.settimeout(0.1)
        sock.connect((ip_address,port))
        print("!!!!! port",port,"is open")
    except:
        print("port",port,"is closed")

print("="*23)
print("welcome to port scanner")
print("="*23)
ip_address = input("enter the ip adress:\n")
port_first = int(input("Enter the first port:\n"))
port_last = int(input("Enter the last port:\n"))
for port in range(port_first,port_last):
    scan_port(ip_address,port)
    
