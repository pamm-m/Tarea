# Programa: Generador de Datos Ficticios con Faker  
# Autor: Pam  
# Descripción:  
#   Este programa utiliza la biblioteca Faker para generar  
#   datos de prueba como nombres, correos, direcciones y  
#   fechas de nacimiento. Su propósito es mostrar cómo  
#   Faker puede crear información realista sin usar datos reales.  

# Importa la clase Faker desde la librería faker
from faker import Faker  

# Crea una instancia (objeto) de Faker con localización en español de México.
# Esto define el idioma y formato de los datos generados.
fake = Faker('es_MX')  # Se podría usar 'es_CR' si se quiere más acorde a Costa Rica


# Define una función que genera una lista de usuarios ficticios
def generar_usuarios(cantidad):  
    """Genera una lista con datos ficticios de usuarios."""  
    
    # Se crea una lista vacía donde se guardarán los usuarios generados
    usuarios = []  
    
    # Bucle que se ejecuta 'cantidad' de veces, según el número de usuarios que se quiera crear
    for i in range(cantidad):  
        
        # Se crea un diccionario con datos generados por Faker
        usuario = {  
            "nombre": fake.name(),  # Genera un nombre completo realista
            "correo": fake.email(),  # Genera una dirección de correo falsa
            "direccion": fake.address(),  # Genera una dirección ficticia
            # Genera una fecha de nacimiento entre 18 y 60 años de edad
            "fecha_nacimiento": fake.date_of_birth(minimum_age=18, maximum_age=60)  
        }  
        
        # Agrega el diccionario del usuario a la lista de usuarios
        usuarios.append(usuario)  
    
    # Devuelve la lista completa con todos los usuarios generados
    return usuarios  


# Bloque principal del programa
# Solo se ejecuta si el archivo se ejecuta directamente y no si se importa como módulo
if __name__ == "__main__":  
    
    # Imprime un encabezado en la consola
    print("=== GENERADOR DE USUARIOS FICTICIOS ===\n")  
    
    # Llama a la función generar_usuarios() para crear 5 usuarios de ejemplo
    lista_usuarios = generar_usuarios(5)  
    
    # Recorre la lista de usuarios y los muestra uno por uno con su información
    for i, usuario in enumerate(lista_usuarios, start=1):  
        print(f"Usuario {i}:")  # Imprime el número del usuario
        print(f"  Nombre: {usuario['nombre']}")  # Muestra el nombre generado
        print(f"  Correo: {usuario['correo']}")  # Muestra el correo electrónico
        print(f"  Dirección: {usuario['direccion']}")  # Muestra la dirección
        print(f"  Fecha de nacimiento: {usuario['fecha_nacimiento']}\n")  # Muestra la fecha de nacimiento
  
    # Imprime un mensaje final indicando que el proceso terminó correctamente
    print("Datos generados correctamente utilizando la biblioteca Faker.")
