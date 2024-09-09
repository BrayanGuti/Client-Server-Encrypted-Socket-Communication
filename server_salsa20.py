import socket
import threading
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
from Crypto.Cipher import Salsa20
import base64

def handle_client(conn):
    key = 'clave_secreta_muy_segura_de_256_'  # 16 bytes exactos    
    while True:
        data = conn.recv(1024).decode()  # Recibir datos del cliente
        if not data:
            break
        decrypt_msg = decrypt_message_salsa20(key, str(data))
        print("De usuario conectado: " + str(decrypt_msg))
        response = input(' -> ')  # Pedir mensaje de respuesta
        encrypt_response = encrypt_message_salsa20(key, response)
        conn.send(encrypt_response.encode())  # Enviar respuesta al cliente

    conn.close()  # Cerrar la conexión con el cliente actual

def server_program():
    host = '0.0.0.0'  # Obtiene el nombre del host
    port = 5000  # Puerto a usar

    server_socket = socket.socket()  
    server_socket.bind((host, port))  
    server_socket.listen(2)  # Escucha hasta 2 clientes simultáneamente

    print(f"Servidor escuchando en {host}:{port}")

    while True:
        conn, address = server_socket.accept()  # Acepta nueva conexión
        print("Conexión desde: " + str(address))
        
        # Crear un hilo para manejar la conexión del cliente
        client_thread = threading.Thread(target=handle_client, args=(conn,))
        client_thread.start()


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
    server_program()