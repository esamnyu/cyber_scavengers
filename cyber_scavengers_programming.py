# https://scavengers.osiris.cyber.nyu.edu/challenges - Challenge Site 
from pwn import *
import time 
import random

host = 'scavengers.osiris.cyber.nyu.edu'
port = 5000

# Establish a connection to the server
s = remote(host, port)

# Loop until we find the safe house or the flag
while True:
    # Receive the data from the server
    data = s.recv()
    print(data.decode())

    # Check if there is a zombie present
    if b'zombie' in data.lower():
        # Send the opposite direction to avoid the zombie
        if b'right' in data.lower():
            s.sendline(b'left')
        elif b'left' in data.lower():
            s.sendline(b'right')
    else:   
        # If there is no zombie, print data 
        print(data.decode())
        # Send a random direction
        s.sendline(random.choice([b'left', b'right']))

    # Check if we found the safe house or the flag
    for line in data.decode().split('\n'):
        if 'flag' in line.lower():
            print("Found the flag!")
            print(line)
            s.close()
            exit()
        # This code should be removed because it just checks the original prompt for the safe house and thinks the safe house is found   
        # if 'safe house' in line.lower():
        #     print("Found the safe house!")
        #     print(line)
        #     s.close()
        #     exit()

    # Add a small delay to avoid overwhelming the server
    time.sleep(0.15)

# Close the connection
s.close()
