from itertools import count
from cryptography.fernet import Fernet
import csv

respuesta = 'Si'
print('Menu')
while respuesta == 'Si' or respuesta == 'si':
    print('1. Cifrar')
    print('2. Descifrar')
    key = Fernet.generate_key()
    fernet = Fernet(key)
    option = str(input('Elija una opción 1 o 2: '))
    text_encrypt = ''
    if option == '1':
        text = str(input('Inserte su mensaje: '))
        text_encrypt = fernet.encrypt(text.encode())
        print('Mensaje original: '+str(text))
        print('Encriptacíón: '+str(text_encrypt))
        print('Clave / Key : '+str(key))
        with open('key.csv', 'w+') as f:
            header = ['key']
            writer = csv.DictWriter(f,fieldnames=header)
            writer.writeheader()
            writer.writerow({'key':key.decode('utf-8')})
        file = open('mensaje_encriptado.txt','wb')
        file.write(text_encrypt)
        file.close()
        respuesta = str(input('Desea realizar otra operacion: Si / No ? '))
        if respuesta == 'No' or respuesta == 'no':
            break
    if option == '2':
        with open('key.csv') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                csv_key = row[0]
                print(Fernet(csv_key))
        with open('mensaje_encriptado.txt','rb') as f:
            raw_data = f.read()
            mensaje_desencriptado = Fernet(csv_key).decrypt(raw_data).decode()                 
        print("Mensaje desencriptado: " + str(mensaje_desencriptado))
        respuesta = str(input('Desea realizar otra operacion Si / No ? '))
        if respuesta == 'No' or respuesta == 'no':
            break