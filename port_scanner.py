import socket

sock = socket.socket()
sock.settimeout(5)

target  = input("Enter the target IP address or hostname: ")
port = input("Enter port: ")
 
try: 
    sock.connect((target, port))
    print( "Port is OPEN")
except:
    print("Port is CLOSED")
finally:
    sock.close()

