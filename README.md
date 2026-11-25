# Proyecto Redis con Python

## Descripción
Sistema de gestión de usuarios desarrollado en Python utilizando Redis como base de datos NoSQL.

## Tecnologías
- Python
- Redis
- Kali Linux
- Redis-py

## Funcionalidades CRUD
1. Registrar usuarios.
2. Consultar usuarios.
3. Modificar usuarios.
4. Eliminar usuarios.

## Estructura de datos
Se utiliza Hash para almacenar nombre, correo y edad de cada usuario.

## Comandos Redis
- PING: comprobar conexión.
- HSET: guardar o modificar datos.
- HGET: consultar un campo.
- HGETALL: consultar todos los campos.
- EXISTS: comprobar si existe una clave.
- DEL: eliminar una clave.

## Ejecución

Iniciar Redis:
sudo systemctl start redis-server

Activar entorno virtual:
source venv/bin/activate

Instalar dependencias:
pip install -r requirements.txt

Ejecutar:
python app.py

## Autora
Verónica De Gracia
