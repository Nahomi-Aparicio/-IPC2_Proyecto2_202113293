
from  Escritorio import Escritorio

class ListaSimpleEscritorio:
    def __init__(self):
        self.inicio = Escritorio()
        self.fin =  Escritorio()
        

    def Agregar(self, NuevoEscritorio):
        if self.inicio.ied is  None:
            self.inicio = NuevoEscritorio
            self.fin = NuevoEscritorio
        elif self.inicio.siguiente is None:
            self.inicio.siguiente = NuevoEscritorio
            self.fin = NuevoEscritorio
        else:
            self.fin.siguiente = NuevoEscritorio
            self.fin = NuevoEscritorio

   
#def optener numero escritorios
    def rerorriendoEs(self):
        contarEsc=0
        aux = self.inicio
        while aux!=None:
            contarEsc+=1
            """print('-------escritorios--------')
            print('ID:',aux.ied)"""
            aux.identificacionEs
            """print('Encargado:',aux.encargadoEs)
            print(" ") """
            aux=aux.siguiente
        self.contarEsc=contarEsc


    def getContarES(self):
        return self.contarEsc

  

    def optener_ultimo(self):
        aux = self.inicio       
        while aux.siguiente != None:            
            aux = aux.siguiente
        return aux


    def ultimoNodo(self):
        aux = self.inicio       
        self.inicio=self.inicio.siguiente                           
        return aux


#todos todos los escritorios aqui 
    def optenerTodos(self):
        aux = self.inicio
        self.inicio=self.inicio.siguiente
        return aux

