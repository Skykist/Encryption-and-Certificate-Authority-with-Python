import os
import base64
from Crypto.Cipher import AES

""" block_size = 16
secretKey = os.urandom(block_size)
print('encryption key: ', secretKey) """

def encrypt(key,secret):
    Block_Size = 16
    Padding = '{'

    pad = lambda s: s + (Block_Size-len(s) % Block_Size) * Padding

    EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))

    cipher = AES.new(key)

    encoded = EncodeAES(cipher, secret)

    #print('Encrypted secret: ',encoded)

    return encoded

def decrypt(key,encSecret):
    Padding = '{'
    DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(Padding)
    cipher = AES.new(key)

    decoded = DecodeAES(cipher, encSecret)

    return decoded
    #print('the secret is ', decoded)

#for testing
#secretMessage = encrypt(secretKey,'hi, keep this a secret. pandas')
#decrypt(secretKey, secretMessage)