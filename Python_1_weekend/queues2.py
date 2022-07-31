class Cola:
    def __init__(self):
        self.__items = []

    def EstaVacia(self):
        if len(self.__items) == 0:
            return True
        else:
            return False

    def Encolar(self, item):
        self.__items.insert(0,item)

    def Desencolar(self):
        return self.__items.pop()

    def LeerPrimerElemento(self):
        return self.__items[len(self.__items) - 1]

    def MostrarCola(self):
        print("Cola: ", self.__items, "<----Primer elemento")

def SimuladorCola():
    fin = False
    cola = Cola()
    while not(fin):
        opc = input("Opcion: ")

        if (opc=='1'):
            item = input("Introduzca el elemento a enconlar: ")
            cola.Encolar(item)
            print("Elemento encolado ", item)

        elif (opc=='2'):
            if cola.EstaVacia():
                print("Cola vacia no hay nada que desencolar")
            else:
                item = cola.LeerPrimerElemento()
                cola.Desencolar()
                print("Elemento desncolado ", item)

        elif (opc=='3'):
            if cola.EstaVacia():
                print("Cola empty")
            else:
                cola.MostrarCola()

print("Simulador de queue")
SimuladorCola()