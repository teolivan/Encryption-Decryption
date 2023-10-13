
import platform
import socket

 #GETHOSTNAME

hostName = platform.node()
print(f"Host name: {hostName}")

#GETHOSTIPADRESS 
hostIPAdress = socket.gethostbyname(socket.gethostname())
print(f"Host IP adress: {hostIPAdress}")