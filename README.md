# 🔐 Client-Server Encrypted Socket Communication

Este proyecto implementa una comunicación cliente-servidor utilizando sockets en Python y un cifrado simétrico AES (CBC mode) con la librería `pycryptodome` para proteger los mensajes. 🛡️

## 🚀 Características

- **Cifrado AES en Modo CBC**: Utiliza un cifrado simétrico AES para asegurar los mensajes entre el cliente y el servidor 🔒.
- **Comunicación Bidireccional**: El cliente y el servidor pueden enviarse mensajes cifrados de ida y vuelta 🔄.
- **Sockets en Python**: Implementación simple y efectiva de la comunicación cliente-servidor.
- **Multihilo**: El servidor puede manejar múltiples clientes simultáneamente mediante hilos.

## 🛠️ Requisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- **Python 3.6 o superior** 🐍
- **Librería `pycryptodome`** para cifrado. Instálala ejecutando este comando:

  ```bash
  pip install pycryptodome
