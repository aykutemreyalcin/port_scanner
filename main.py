import socket

open_port_list = []
def scan_port(ip_address, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.05)
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
                print("!!!!! Port", port, "is open. Service:", service)
                open_port_list.append(port)
                open_port_list.append(service)
                with open("port_list.txt", "a") as file:
                    file.write(f"Port {port} is open. Service: {service}\n")
                
            except:
                print("!!!!! Port", port, "is open. Service: Unknown")
                open_port_list.append(port)
                open_port_list.append("Unknown")
                with open("port_list.txt", "a") as file:
                    file.write(f"Port {port} is open. Service: {service}\n")
        else:
            print("Port", port, "is closed")
    except socket.error as err:
        print("Socket error:", err)
    finally:
        sock.close()

print("="*23)
print("Welcome to Port Scanner")
print("="*23)
ip_address = input("Enter the IP address:\n")
port_first = int(input("Enter the first port:\n"))
port_last = int(input("Enter the last port:\n"))
for port in range(port_first, port_last + 1): 
    scan_port(ip_address, port)
print("="*30)
for i in range(1,len(open_port_list)+1,2):
    print("port",open_port_list[i-1],"--------->",open_port_list[i])

print("Open ports have been saved ")



