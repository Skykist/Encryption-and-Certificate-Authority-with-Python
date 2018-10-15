import socket
from encryptor import encrypt,decrypt
import sys
import os
import base64
from Crypto.Cipher import AES
from ca import isCertValid

reload(sys)
sys.setdefaultencoding("ISO-8859-1")

def connectAndSend(msg):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server = "192.168.0.9"
    port = 9500
    sock.connect((server,port))

    sock.send(msg.encode())
    message = sock.recv(1024).decode()
    #print(message)

    sock.close()

    return message

#creates key for encryptying messages
block_size = 16
secretKey = os.urandom(block_size)
print('The encryption key: '+ secretKey)

print('\nRequesting certificate....')
cert = connectAndSend("requesting cert")
if isCertValid(cert):
    print("certificate is valid")
    connectAndSend(secretKey)
else:
    print("certificate is not valid\n")
    connectAndSend("Goodbye")

def sendEncryMsg(key,message):
    secretMsg = encrypt(key,message)
    print("\nSending secret message...")
    response = connectAndSend(secretMsg)
    print("Response back: "+response)
    print("Decrypted response: "+decrypt(key,response))

sendEncryMsg(secretKey,"Hi, can you encryp this?")
sendEncryMsg(secretKey,"Copying me doesn't prove anything.")