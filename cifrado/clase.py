import csv
from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)
mensaje = "Este es un mensaje super secreto"
mensaje_secreto = fernet.encrypt(mensaje.encode())

print('original: ', mensaje)
print('encriptacion: ', mensaje_secreto)
print('key: ', key)
with open('key.csv', 'w+') as f:
    header = ['key']
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    writer.writerow({'key': key.decode('utf-8')})
file = open('message_encryoted.txt', 'wb')
file.write(mensaje_secreto)
file.close()
with open('key.csv') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        csv_key = row[0]
        print(Fernet(csv_key))
        with open('message_encryoted.txt', 'rb') as f:
            raw_data = f.read()
            mensaje_desencriptado = Fernet(csv_key).decrypt(raw_data).decode()
print('mensaje desencriptado desde los archivos')
print(mensaje_desencriptado)
