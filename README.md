# Secure-Chat-Application

Client python code on User's machine and server python code on the machine which you want to set up as server.

** Works in Both Windows as Well as Linux operating systems.

Requirements

Install Pycrypto library
Install Python 2.7 or 3.1

Features
---------------------------------------------
1] Selective AES Encryption

2] MUltithreading support

3] TCP protocol for communication

4] 256 bit key used for encryption 

5] Chat simultaneously with 100 clients.


Description
---------------------------------------------
Basically multithreadedserver.py sets up the server listening on a port and similarly clientlocalhost.py sets up the client to connect to that port on which server is listening by providing ip address of the server and port, 256 bit key is provided with 16byte iv for Selective AES encryption , you can change the key and iv  as per your requirements, you just need to type "quit" to get logged out.This whole setup works on TCP connection,always preferred over udp even though slow but reliable.
