import socket
import time


target  = input("Enter the target IP address or hostname: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))
open_ports = []
start_time = time.time()
 
print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

#scanning ports in range
for port in range(start_port, end_port + 1):
    sock = socket.socket()
    sock.settimeout(0.5)
    try:
        sock.connect((target, port))
        print(f"Port {port} is OPEN")
        open_ports.append(port)
    except:
        pass
    finally:
        sock.close()

#calculate scanning time   
end_time = time.time()
scan_time = end_time - start_time

#print summary
print(f"\nScan complete in {scan_time:.2f} seconds.")
if open_ports:
    print("Open ports found:" , ", ".join(str(p) for p in open_ports))
else:
    print("No open ports found in the given range.")