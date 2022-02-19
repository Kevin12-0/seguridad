import Crypto
import binascii
from Crypto.PublicKey import  RSA
from Crypto.Cipher import PKCS1_OAEP


respuesta = 'si'
message = ''
message_des = ''
cipher_text = ''
cipher_text2 = ''
cipher_text3 = ''
#generar claves diferentes con random
random_generator = Crypto.Random.new().read
#clave 1
private_key = RSA.generate(1024, random_generator)
public_key = private_key.public_key()
public_key2 = private_key.public_key()
public_key3 = private_key.public_key()
    
private_key = private_key.exportKey(format='DER')
public_key = public_key.exportKey(format='DER')
public_key2 = public_key2.exportKey(format='DER')
public_key3 = public_key3.exportKey(format='DER')

private_key = binascii.hexlify(private_key).decode('utf-8')
public_key = binascii.hexlify(public_key).decode('utf-8')
public_key2 = binascii.hexlify(public_key2).decode('utf-8')
public_key3 = binascii.hexlify(public_key3).decode('utf-8')

private_key = RSA.importKey(binascii.unhexlify(private_key))
public_key = RSA.importKey(binascii.unhexlify(public_key))
public_key2 = RSA.importKey(binascii.unhexlify(public_key2))
public_key3 = RSA.importKey(binascii.unhexlify(public_key3))

with open('ClavePrivada1.pem','w') as pr:
    pr.write(str(private_key))
with open('ClavePublica1.pem','w') as pub:
    pub.write(str(public_key))
with open('ClavePublica2.pem','w') as pub2:
    pub2.write(str(public_key2))
with open('ClavePublica3.pem','w') as pub3:
    pub3.write(str(public_key3))
    
while respuesta == 'Si' or respuesta == 'si':
    print('bienvendio elija una opción')
    print('1. Cifrar')
    print('2. Descifrar')
    opcion = str(input('1/2: '))
    
    if opcion == '1':
        message = input('Inserte su mensaje: ')
        message = message.encode(encoding='utf-8')
        
        cipher = PKCS1_OAEP.new(public_key)
        cipher_text = cipher.encrypt(message)
        print(cipher_text)
        print("")
        #encriptacion de clave 2
        cipher2 = PKCS1_OAEP.new(public_key2)
        cipher_text2 = cipher.encrypt(message)
        print(cipher_text2)
        print("")
        #encriptacion de clave 3
        cipher3 = PKCS1_OAEP.new(public_key3)
        cipher_text3 = cipher.encrypt(message)
        print(cipher_text3)
        respuesta = str(input('Desea realizar otra operacion Si / No ?: '))
        if respuesta == 'No' or respuesta == 'no':
            break
    if opcion == '2':
        clave_elejir = str(input('Elige la clave con la cual quieres descifrar el mensaje: 1,2 o 3: '))
        if clave_elejir == '1':
            cipher = PKCS1_OAEP.new(private_key)
            message_des = cipher.decrypt(cipher_text)
            print(message_des)
            respuesta = str(input('Desea realizar otra operacion Si / No ?: '))
            if respuesta == 'No' or respuesta == 'no':
                break
        elif clave_elejir == '2':
            cipher = PKCS1_OAEP.new(private_key)
            message_des = cipher.decrypt(cipher_text2)
            print(message_des)
            respuesta = str(input('Desea realizar otra operacion Si / No ?: '))
            if respuesta == 'No' or respuesta == 'no':
                break
        elif clave_elejir == '3':
            cipher = PKCS1_OAEP.new(private_key)
            message_des = cipher.decrypt(cipher_text3)
            print(message_des)
            respuesta = str(input('Desea realizar otra operacion Si / No ?: '))
            if respuesta == 'No' or respuesta == 'no':
                break