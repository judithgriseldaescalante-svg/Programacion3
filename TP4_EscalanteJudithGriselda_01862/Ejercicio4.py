#Ejercicio Nro 4: Gestión de Inventario de Instrumentos Musicales
#Una fábrica de instrumentos musicales posee diferentes sucursales. Cada sucursal tiene un
#nombre y una lista de instrumentos disponibles para la venta.
#De cada instrumento se conoce:
# ID: identificador alfanumérico.
#Precio: precio del instrumento.
#Tipo: puede ser Percusión, Viento o Cuerda.
#Implementar una solución que permita gestionar el inventario.
#Requisitos
#1. listarInstrumentos()
#Mostrar en la consola todos los instrumentos disponibles, indicando sucursal, ID, precio y
#tipo.
#2. instrumentosPorTipo(tipo)
#Recibir como parámetro un tipo de instrumento y devolver una lista con los instrumentos
#que pertenecen a ese tipo.
#3. borrarInstrumento(id)
#Recibir un ID y eliminar el instrumento correspondiente de la sucursal en la que se
#encuentre.
#4. porcInstrumentosPorTipo(sucursal)
#Recibir el nombre de una sucursal y mostrar o retornar el porcentaje de instrumentos
#correspondientes a cada tipo:
#o Percusión
#o Viento
#o Cuerda
class Sucursal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.instrumentos = []

    def agregar_instrumento(self, instrumento):
        self.instrumentos.append(instrumento)

def mostrar_instrumentos(inventario):
    print("INVENTARIO: ")
    for sucursal in inventario:
        for instrumento in sucursal.instrumentos:
            print(f" {sucursal.nombre}, ID: {instrumento['ID']}, {instrumento['Precio']} {instrumento['Tipo']}")

def instrumentosPorTipo(inventario, tipo):
    encontrados = []
    for sucursal in inventario:
        for instrumento in sucursal.instrumentos:
            if instrumento["Tipo"] == tipo:
                encontrados.append(instrumento)
    return encontrados

def borrarInstrumento(inventario, id):
    for sucursal in inventario:
        for instrumento in sucursal.instrumentos:
            if instrumento["ID"] == id:
                sucursal.instrumentos.remove(instrumento)
                print(f"Instrumento {id} eliminado")
                return
    print(f"El ID {id} no se encontro en el inventario")

def porcInstrumentosPorTipo(inventario, nombre_sucursal):
    for sucursal in inventario:
        if sucursal.nombre == nombre_sucursal:
            total = len(sucursal.instrumentos)
            if total == 0:
                print(f"La sucursal {nombre_sucursal} no tiene instrumentos")
                return
            percucion, viento, cuerda = 0, 0, 0
            for instrumento in sucursal.instrumentos:
                if instrumento["Tipo"] == "Percusion":
                    percucion += 1
                elif instrumento["Tipo"] == "Viento":
                    viento += 1
                elif instrumento["Tipo"] == "Cuerda":
                    cuerda += 1
            print(f"Porcentaje en {nombre_sucursal}:")
            print(f"Percusion: {(percucion / total) * 100}")
            print(f"Viento: {(viento / total) * 100}")
            print(f"Cuerda: {(cuerda / total) * 100}")
            return
    print(f"No se encontro la sucursal {nombre_sucursal}")

def main():
    suc1 = Sucursal("Music Store")
    carga_suc1 = [
        {"ID": "G77", "Precio": 50000, "Tipo": "Cuerda"},
        {"ID": "B12", "Precio": 35000, "Tipo": "Percusion"},
        {"ID": "C17", "Precio": 90000, "Tipo": "Cuerda"}
    ]
    for inst in carga_suc1:
        suc1.agregar_instrumento(inst)

    suc2 = Sucursal("Galeria del arte")
    carga_suc2 = [
        {"ID": "F01", "Precio": 42000, "Tipo": "Viento"},
        {"ID": "C99", "Precio": 60000, "Tipo": "Cuerda"},
        {"ID": "V88", "Precio": 45000, "Tipo": "Viento"},
        {"ID": "J22", "Precio": 170000, "Tipo": "Percusion"}
    ]
    for inst in carga_suc2:
        suc2.agregar_instrumento(inst)
    inventario = [suc1, suc2]
    while True:
        print("1. Ver inventario completo")
        print("2. Buscar instrumentos por Tipo")
        print("3. Borrar un instrumento por id")
        print("4. Ver porcentaje de instrumentos en sucursal")
        print("5. Salir")

        opcion = input("Elegi una opción: ")
        if opcion == "1":
            mostrar_instrumentos(inventario)
        elif opcion == "2":
            tipo_buscado = input("Ingrese el tipo que busca:")
            resultado = instrumentosPorTipo(inventario, tipo_buscado)
            if len(resultado) > 0:
                print(f"Encontrados {tipo_buscado}:")
                for instrumento in resultado:
                    print(instrumento)
            else:
                print(f"No se encontro instrumentos de {tipo_buscado}")
        elif opcion == "3":
            id = input("Ingrese el ID: ")
            borrarInstrumento(inventario, id)
        elif opcion == "4":
            sucursal = input("Ingrese el nombre de la sucursal: ")
            porcInstrumentosPorTipo(inventario, sucursal)
        elif opcion == "5":
            break
        else:
            print("Opcion no valida")

main()