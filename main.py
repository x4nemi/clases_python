from paqueteria import Paqueteria
from paquete import Paquete

# p = Paquete()
# p._Paquete__id = "100"
# print(p._Paquete__id) #acceder a un atributo privado

p = Paqueteria()

while True:
    print("1) Agregar")
    print("2) Mostrar")
    print("0) Salir")
    op = input("Opcion: ")

    if op == "1":
        id = input("Id: ")
        origen = input("Origen: ")
        destino = input("Destino: ")
        peso = float(input("Peso: "))

        paquete = Paquete(id, origen, destino, peso)

        p.agregar(paquete)
        print("Aregado...")
    if op == "2":
        p.mostrar()
    if op == "0":
        break