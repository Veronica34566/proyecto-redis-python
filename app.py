

import redis

# =====================================
# CONEXION CON REDIS
# =====================================

conexion = redis.Redis(
    host='localhost',
    port=6379,
    decode_responses=True
)

# Comprobar conexion
try:
    conexion.ping()
    print("\nConexion con Redis exitosa")

except redis.ConnectionError:
    print("Error: No se pudo conectar con Redis")
    exit()


# =====================================
# 1. REGISTRAR USUARIO
# =====================================

def registrar_usuario():

    print("\n--- REGISTRAR USUARIO ---")

    identificador = input("ID del usuario: ").strip()

    if not identificador:
        print("El ID es obligatorio")
        return

    clave = f"usuario:{identificador}"

    if conexion.exists(clave):
        print("Este usuario ya existe")
        return

    nombre = input("Nombre: ").strip()
    correo = input("Correo: ").strip()
    edad = input("Edad: ").strip()

    if not nombre or not correo or not edad:
        print("Todos los campos son obligatorios")
        return

    if not edad.isdigit():
        print("La edad debe ser un numero")
        return

    conexion.hset(
        clave,
        mapping={
            "nombre": nombre,
            "correo": correo,
            "edad": edad
        }
    )

    print("\nUsuario registrado correctamente")


# =====================================
# 2. CONSULTAR USUARIO
# =====================================

def consultar_usuario():

    print("\n--- CONSULTAR USUARIO ---")

    identificador = input("ID del usuario: ").strip()

    usuario = conexion.hgetall(f"usuario:{identificador}")

    if usuario:
        print("\nDATOS DEL USUARIO")
        print("Nombre:", usuario["nombre"])
        print("Correo:", usuario["correo"])
        print("Edad:", usuario["edad"])

    else:
        print("Usuario no encontrado")


# =====================================
# 3. MODIFICAR USUARIO
# =====================================

def modificar_usuario():

    print("\n--- MODIFICAR USUARIO ---")

    identificador = input("ID del usuario: ").strip()
    clave = f"usuario:{identificador}"

    if not conexion.exists(clave):
        print("Usuario no encontrado")
        return

    nombre = input("Nuevo nombre: ").strip()
    correo = input("Nuevo correo: ").strip()
    edad = input("Nueva edad: ").strip()

    if not nombre or not correo or not edad:
        print("Todos los campos son obligatorios")
        return

    if not edad.isdigit():
        print("La edad debe ser un numero")
        return

    conexion.hset(
        clave,
        mapping={
            "nombre": nombre,
            "correo": correo,
            "edad": edad
        }
    )

    print("Usuario modificado correctamente")


# =====================================
# 4. ELIMINAR USUARIO
# =====================================

def eliminar_usuario():

    print("\n--- ELIMINAR USUARIO ---")

    identificador = input("ID del usuario: ").strip()

    eliminado = conexion.delete(f"usuario:{identificador}")

    if eliminado:
        print("Usuario eliminado correctamente")
    else:
        print("Usuario no encontrado")


# =====================================
# MENU PRINCIPAL
# =====================================

while True:

    print("\n================================")
    print("     SISTEMA DE USUARIOS REDIS")
    print("================================")
    print("1. Registrar usuario")
    print("2. Consultar usuario")
    print("3. Modificar usuario")
    print("4. Eliminar usuario")
    print("5. Salir")

    opcion = input("\nSeleccione una opcion: ").strip()

    if opcion == "1":
        registrar_usuario()

    elif opcion == "2":
        consultar_usuario()

    elif opcion == "3":
        modificar_usuario()

    elif opcion == "4":
        eliminar_usuario()

    elif opcion == "5":
        print("Cerrando el sistema...")
        break

    elif opcion == "":
        print("Debe seleccionar una opcion")

    else:
        print("Opcion no valida. Intente nuevamente")


