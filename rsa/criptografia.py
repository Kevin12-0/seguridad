import Crypto
import binascii
from Crypto.PublicKey import  RSA
from Crypto.Cipher import PKCS1_OAEP

random_generator = Crypto.Random.new().read

private_key = RSA.generate(1024, random_generator)
public_key = private_key.public_key()

private_key = private_key.exportKey(format='DER')
public_key = public_key.exportKey(format='DER')

private_key = binascii.hexlify(private_key).decode('utf-8')
public_key = binascii.hexlify(public_key).decode('utf-8')


#proceso inverso

private_key = RSA.importKey(binascii.unhexlify(private_key))
public_key = RSA.importKey(binascii.unhexlify(public_key))

message = 'Hola Mundo'

message = message.encode()
cipher = PKCS1_OAEP.new(public_key)
cipher_message = cipher.encrypt(message)

print(cipher_message)

# desencriptar

cipher = PKCS1_OAEP.new(private_key)
message_des = cipher.decrypt(cipher_message)
print(message_des)

