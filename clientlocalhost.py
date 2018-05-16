import socket
import threading 
from Crypto.Cipher import AES
i="192.168.43.59"
sock =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print "Ports on network"
for p in xrange(8080,8090):
    sock =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    result = sock.connect_ex((i,p))
    if result==0:
        sock.send("ping_tester")
        ok=sock.recv(4096)
        print p," Ready"
    else:
        print p," Unavailable"
    sock.close()
port=input()
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((i,port))
response1=client.recv(4096)
print "" 
print response1
b=raw_input("\n[*]Enter your name->")
client.send(b)
ok=client.recv(4096)
print ok
key = b'\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18'
iv = "abcdefghijklmnop"
def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)
def encrypt(message,iv,key):
    message = pad(message)
    cipher = AES.new(key, AES.MODE_CBC,iv)
    return cipher.encrypt(message)
def decrypt(ciphertext,key,iv):
    	cipher = AES.new(key, AES.MODE_CBC,iv)
    	plaintext = cipher.decrypt(ciphertext)
    	return plaintext.rstrip(b"\0")
def message_send():
	while True:
                a=raw_input("[*]Enter Message to send to everyone-->")
                encrypted_message=encrypt(a,iv,key)
    		if(a=="quit"):
                        client.send(encrypted_message)
                        print "\n[You are Logged out from chat room]"
                        break
    		else:
        		client.send(encrypted_message)
        client.close() 
def message_response():
        while True:
        	response=client.recv(4096)
                if "quitted" in response:
                	break
                else:
                	decrypted_message=decrypt(response,key,iv)
                	print "\n%s" %(decrypted_message)
                	print "::Type [Below] to send message to everyone::"
	client.close()
if __name__=='__main__':
	threading.Thread(target=message_send).start()
        threading.Thread(target=message_response).start()
