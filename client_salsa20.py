import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
from Crypto.Cipher import Salsa20
import base64


def client_program():
    host = '172.20.10.3'  # Cambiado a localhost para ejecutar en la misma máquina
    port = 5000  # Número de puerto del servidor

    client_socket = socket.socket()  # Instanciar socket
    client_socket.connect((host, port))  # Conectar al servidor
    key = 'clave_secreta_muy_segura_de_256_'  # Clave de 16 bytes
    message = input(" -> ")  # Tomar entrada del usuario

    while message.lower().strip() != 'bye':
        encrypted = encrypt_message_salsa20(key, message)
        client_socket.send(encrypted.encode())  # Enviar mensaje
        data = client_socket.recv(1024).decode()  # Recibir respuesta

        decrypt_data = decrypt_message_salsa20(key, data) # Desencriptar mensaje
        print('Recibido del servidor: ' + decrypt_data)  # Mostrar en terminal

        message = input(" -> ")  # Volver a tomar entrada

    client_socket.close()  # Cerrar la conexión


# Función para encriptar un mensaje usando Salsa20
def encrypt_message_salsa20(key, message):
    # Convertir la clave a bytes (debe ser de 32 bytes para Salsa20)
    key = key.encode('utf-8')
    
    # Generar un nonce aleatorio de 8 bytes
    cipher = Salsa20.new(key=key)
    nonce = cipher.nonce
    
    # Cifrar el mensaje
    encrypted_message = cipher.encrypt(message.encode('utf-8'))
    
    # Devolver el mensaje cifrado junto con el nonce
    return base64.b64encode(nonce + encrypted_message).decode('utf-8')

# Función para desencriptar un mensaje usando Salsa20
def decrypt_message_salsa20(key, encrypted_message):
    # Convertir la clave a bytes
    key = key.encode('utf-8')
    
    # Decodificar el mensaje en base64
    encrypted_message = base64.b64decode(encrypted_message)
    
    # Extraer el nonce (los primeros 8 bytes)
    nonce = encrypted_message[:8]
    ciphertext = encrypted_message[8:]
    
    # Crear el descifrador Salsa20 con el mismo nonce
    cipher = Salsa20.new(key=key, nonce=nonce)
    
    # Desencriptar el mensaje
    decrypted_message = cipher.decrypt(ciphertext)
    
    return decrypted_message.decode('utf-8')

if __name__ == '__main__':
    client_program()

