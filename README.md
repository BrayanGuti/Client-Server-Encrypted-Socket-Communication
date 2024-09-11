# 🔐 Client-Server Encrypted Socket Communication

Este proyecto implementa una comunicación cliente-servidor utilizando sockets en Python y un cifrado simétrico AES (CBC mode) o Salsa20 con la librería `pycryptodome` para proteger los mensajes. 🛡️

## 🚀 Características

- **Cifrado AES en Modo CBC y Salsa20**: Utiliza un cifrado simétrico AES o Salsa20 para asegurar los mensajes entre el cliente y el servidor 🔒.
- **Envio de Clave Desencriptada**: La primera comunicación entre el cliente y el servidor es el envío de la clave simétrica Salsa20 sin cifrar. Posteriormente, todos los mensajes se cifran usando esa clave. Esta clave se acuerda al principio y permite la encriptación y desencriptación de los mensajes a partir de ese punto 🔑.
- **Comunicación Bidireccional**: El cliente y el servidor pueden enviarse mensajes cifrados de ida y vuelta 🔄.
- **Sockets en Python**: Implementación simple y efectiva de la comunicación cliente-servidor.
- **Multihilo**: El servidor puede manejar múltiples clientes simultáneamente mediante hilos.

## 🛠️ Requisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- **Python 3.6 o superior** 🐍
- **Librería `pycryptodome`** para cifrado. Instálala ejecutando este comando:

  ```bash
  pip install pycryptodome
