#Ejercicio3
#Registro de Información en un Diccionario.
#Requisitos:
#1. Solicitar al usuario que ingrese los siguientes datos: nombre, edad, dirección y teléfono.
#2. Almacenar los datos en un diccionario llamado usuario_info.
#3. Permitir el ingreso de información para varios usuarios.
#4. Mostrar la información ingresada para cada usuario en formato clave-valor.
def main():
    usuario=1
    cantidad=int(input("Cuantos usuarios desea ingresar?: "))
    usuario_info={}
    while (usuario<=cantidad):
        print(f"Usuario {usuario}")
        nombre=(input("Ingrese su nombre: "))
        edad=int(input("Ingrese su edad: "))
        direccion=(input("Ingrese su direccion: "))
        telefono=(input("Ingrese su telefono: "))
        usuario_info [f"Usuario {usuario}"]={"Nombre":nombre, "Edad":edad, "Direccion":direccion, "Telefono":telefono}
        usuario+=1

    for key,value in usuario_info.items():
        print (key,value)

main()