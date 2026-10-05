# Ejercicio1
# Validación de entrada y búsqueda en una Lista.
#Implementar un programa que valide la entrada de un número entero y verifique su presencia en
#una lista.
#Requisitos:
#1. Solicitar al usuario que ingrese un número entero del 0 al 9.
#2. Mientras el número ingresado no esté en el rango especificado, repetir la solicitud.
#3. Verificar si el número se encuentra en una lista predefinida de números.
#4. Notificar al usuario si el número está o no en la lista.
#Concepto útil: Utilizar la sintaxis [valor] in [lista] para comprobar la presencia de un valor en una
#lista.
def main ():
    numero= validar_numero()
    verificar_numero(numero)
def validar_numero():
    while(True):
        num= int(input("Ingrese un numero entero: "))
        if(num<0 or num>9):
            print("El numero debe ser entre 0 y 9")
        else:
            print(f"Numero {num} valido")
            return num

def verificar_numero(num):
    numeros = [2, 4, 8, 5]
    if num in numeros:
        print(f"El numero {num} se encuentra en la lista")
    else:
        print(f"El numero {num} no se encuentra en la lista")
main()