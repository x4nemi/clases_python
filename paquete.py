class Paquete:
    def __init__(self, id, origen, destino, peso): #constructor con sus atributos
        self.__id = id #_protegida
        self.__origen = origen #__privada
        self.__destino = destino #pública
        self.__peso = peso
    
    def imprimir(self):
        print("Id: ", self.__id)
        print("Origen: ", self.__origen)
        print("Destino: ", self.__destino)
        print("Peso: ", self.__peso)
