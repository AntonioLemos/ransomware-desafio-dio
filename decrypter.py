import os
import pyaes

file_name = 'teste.txt.ransomwaretroll'

with open(file_name, 'rb') as file:
    file_data = file.read()

key = b'0123456789abcdef0123456789abcdef'

aes = pyaes.AESModeOfOperationCTR(key)

decrypt_data = aes.decrypt(file_data)

os.remove(file_name)

new_file = 'teste.txt'

with open(new_file, 'wb') as file:
    file.write(decrypt_data)

print(f'Arquivo descriptografado como {new_file}')
