from ListaSimpEscritorio import ListaSimpleEscritorio
class PuntoAtencion:
    def __init__(self,idA=None, nombre=None, direccion=None):
        self.idA=idA
        self.nombre = nombre
        self.direccion = direccion
        self.Escritorios = ListaSimpleEscritorio()
        self.siguiente = None

    def getIdA(self):
        return self.idA

    def getNombre(self):
        return self.nombre

    def getDireccion(self):
        return self.direccion

    def  setIdA(self,idA):
        self.idA=idA

    def setNombre(self,nombre):
        self.nombre=nombre

    def setDireccion(self,direccion):
        self.direccion=direccion

    

    
       
   