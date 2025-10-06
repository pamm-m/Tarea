
# Programa: Generador de Datos Ficticios con Faker
# Autor: Felipe (estudiante)
# Descripción:
#   Este programa utiliza la biblioteca Faker para generar
#   datos de prueba como nombres, correos, direcciones y
#   fechas de nacimiento. Su propósito es mostrar cómo
#   Faker puede crear información realista sin usar datos reales.


# Importar la biblioteca Faker
from faker import Faker

# Crear un objeto Faker en español (Costa Rica)
fake = Faker('es_MX')  # Español de México



# Función para generar una lista de usuarios ficticios

def generar_usuarios(cantidad):
    """Genera una lista con datos ficticios de usuarios."""
    usuarios = []
    for i in range(cantidad):
        usuario = {
            "nombre": fake.name(),
            "correo": fake.email(),
            "direccion": fake.address(),
            "fecha_nacimiento": fake.date_of_birth(minimum_age=18, maximum_age=60)
        }
        usuarios.append(usuario)
    return usuarios


# Programa principal

if __name__ == "__main__":
    print("=== GENERADOR DE USUARIOS FICTICIOS ===\n")

    # Generar 5 usuarios de ejemplo
    lista_usuarios = generar_usuarios(5)

    # Mostrar los resultados en pantalla
    for i, usuario in enumerate(lista_usuarios, start=1):
        print(f"Usuario {i}:")
        print(f"  Nombre: {usuario['nombre']}")
        print(f"  Correo: {usuario['correo']}")
        print(f"  Dirección: {usuario['direccion']}")
        print(f"  Fecha de nacimiento: {usuario['fecha_nacimiento']}\n")

    print("Datos generados correctamente utilizando la biblioteca Faker.")
