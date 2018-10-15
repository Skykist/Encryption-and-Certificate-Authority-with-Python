import socket
from encryptor import encrypt,decrypt
import sys
import os
import base64
from Crypto.Cipher import AES

reload(sys)
sys.setdefaultencoding("ISO-8859-1")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "192.168.0.9"
port = 9500
sock.bind((server,port))

cert = open("my_cert.crt","r").read()

key = None
print("waiting for certificate request..")

sock.listen(5)
print("the server is listening...\n")

c, addr = sock.accept()
print("Connection established")

message = c.recv(1024).decode()
print("Message received")
print("It is: "+ message)
    
if message =='requesting cert':
    c.send(cert.encode())
    print('certificate sent\n')
    
    print ("waiting for key..")
    sock.listen(5)
    c, addr = sock.accept()
    print("Connection established")

    message = c.recv(1024).decode()
    print("Message received")
        
    if message =='Goodbye':
        c.send("okay".encode())     
    else:
        key = message
        print('Key received!\n')
        c.send("Thanks for the key!".encode())      
else:
    c.send("okay".encode())

while True:

    sock.listen(5)
    print("the server is listening...\n")

    c, addr = sock.accept()
    print("Connection established")

    message = c.recv(1024).decode()
    print("Message received")
    print("It is: "+ message)
    
    decryMsg = decrypt(key,message)
    encryMsg = encrypt(key,decryMsg)

    c.send(encryMsg.encode())

    print("Response sent\n")

c.close()
sock.close()
