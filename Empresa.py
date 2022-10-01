from ListapuntoA import ListaSimpleAtencion
from listaTranses import listaSimpleTranses
class Empreza:
    def __init__(self,id=None,nombre=None,abrev=None):
        self.id = id
        self.nombre = nombre
        self.abrev = abrev
        self.listaPuntoAtencion = ListaSimpleAtencion()
        self.listaTrans=listaSimpleTranses()        
        self.siguiente = None

    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getAbrev(self):
        return self.abrev

    def  setId(self,id):
        self.id=id

    def setNombre(self,nombre):
        self.nombre=nombre

    def setAbrev(self,abrev):
        self.abrev=abrev




       