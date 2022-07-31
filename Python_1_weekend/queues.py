class Pila:
    def __init__(self):
        self.__items = []

    def EstaVacia(self):
        if len(self.__items) == 0:
            return True
        else:
            return False

    def Apilar(self, item):
        self.__items.append(item)
    def Retirar(self):
        return self.__items.pop()

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

    def MostrarCola(self):
        print("Cola: ", self.__items, "<----Primer elemento")

cola = Cola()

for i in range(10):
    cola.Encolar(i)
cola.MostrarCola()

pila = Pila()
while not(cola.EstaVacia()):
    pila.Apilar(cola.Desencolar())
while not(pila.EstaVacia()):
    cola.Encolar(pila.Retirar())

cola.MostrarCola()
