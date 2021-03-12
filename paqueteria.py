class Paqueteria:
    def __init__(self):
        self.__lista = []

    def agregar(self, paquete):
        self.__lista.append(paquete)

    def mostrar(self):
        for p in self.__lista:
            p.imprimir()
