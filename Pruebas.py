import names
import random

def generarNombre():
    nombre = names.get_first_name()
    apellido = names.get_last_name()
    apellido2 = names.get_last_name()
    return nombre + " " + apellido + " " + apellido2

def generarTelefono():
    x = random.randint(0, 99999999)
    if x // 1000000 == 9 or x // 1000000 == 8 or x // 1000000 == 7 or x // 1000000 == 6:
        return x
    else:
        return generarTelefono()

print(generarTelefono())