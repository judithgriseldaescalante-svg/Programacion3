#Ejercicio2
#Gestión de Conjuntos de Usuarios y Administradores
#Requisitos:
#1. Crear un conjunto llamado usuarios con los nombres: Marcela, David, Elvira, Juan, y
#Marcos.
#2. Crear un conjunto llamado administradores con los nombres: Juan y Marcela.
#3. Eliminar a Juan del conjunto de administradores.
#4. Añadir a Marcos como administrador, pero mantenerlo en el conjunto de usuarios.
#5. Mostrar todos los usuarios, indicando si cada uno es administrador o no.

def main():
    usuarios={"Marcela","David","Elvira","Juan","Marcos"}
    administradores= {"Juan","Marcela"}
    administradores.discard("Juan")
    administradores.add("Marcos")
    print(f"USUARIOS: {usuarios}")
    print(f"ADMINISTRADORES: {administradores}")
    for usuario in usuarios:
        if(usuario in administradores):
            print(f"{usuario} es usuario y tambien un administrador")
        else:
            print(f"{usuario} es solo usuario")
main()