WAP to create a simple client-server application. Server CODE:
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) port = 9999
server.bind(("localhost", port))

server.listen(1)
print("Waiting for connection")
 
conn, addr = server.accept() print("Connected to: ",addr)

data = conn.recv(1024) print("Client says: ",data.decode())

conn.send("Hello Client".encode()) conn.close()
Client code:
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) port = 9999
client.connect(("localhost", port))

client.send("Hello Server".encode())
data = client.recv(1024) print("Server says: ",data.decode())
client.close()



Objective: WAP to send time from the server and print on the client every second. Your Task: Make the time to print on the same line.

Server code:
import socket import time
from datetime import datetime print("\nServer machine")
 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname() port = 9999
sock.bind((host_name, port)) sock.listen(1)
print("\nWaitng for connection")
conn, addr = sock.accept() print("\nConnection from: ",addr)
while True:
current_time = datetime.now().strftime("%H:%M:%S") conn.send(current_time.encode())
time.sleep(1) Client Code:
import socket print("\nClient machine")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname() port = 9999
sock.connect((host_name, port)) while True:
data = sock.recv(1024) if not data:
break
print("\nTime sent from server: ",data.decode())



WAP to create a Chat Application running on the same machine
Server Code:
import socket print("\nServer machine")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_name = socket.gethostname() port = 9999

server.bind((host_name, port)) server.listen(1)

print(f"\nServer listening on {host_name} : {port}") conn, client_addr = server.accept() print("\nConnection to: ", client_addr)
conn.send("Hello Client!! Welcome to the chat. type 'exit' to quit.".encode()) try:
while True:
client_msg = conn.recv(1024).decode().strip() if not client_msg:
print("Client Disconnected.") break

print("Clien: ",client_msg)

if client_msg.lower() == "exit": conn.send("exit".encode()) print("Chat ended by client")
 
break
server_msg = input("server: ").strip() conn.send(server_msg.encode())

if server_msg.lower() == "exit": print("Chat ended by server") break
except KeyboardInterrupt: print("\nServer Interrupted")
finally:
conn.close() server.close()
Client Code:
import socket print("\nClient machine")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_name = socket.gethostname() port = 9999
client.connect((host_name, port))
greeting = client.recv(1024).decode() print("Server: ",greeting)

try:
while True:
msg = input("Client: ").strip() client.send(msg.encode())
if msg.lower() == "exit": print("You ended the chat") break
reply = client.recv(1024).decode().strip() if not reply:
print("Server disconnected")
break

if reply.lower() == "exit": print("Server ended the chat") break

print("Server: ", reply)
 
except KeyboardInterrupt: print("\nClient Interrupted")

finally:
client.close()


