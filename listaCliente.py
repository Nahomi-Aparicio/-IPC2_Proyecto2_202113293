from lista_inicialTranse import listaSimpleTransess
from lista_inicialTranse import TranseNodo
class ClientesNodo:
    def __init__(self, dpi=None,nombre=None):
        self.dpi = dpi   
        self.nombre = nombre
        self.transs=listaSimpleTransess()   
        self.siguiente=None
        

class listaSimpleClientes:
    def __init__(self):
        self.inicio = ClientesNodo()
        self.fin =  ClientesNodo()
        

    def Agregar(self, NuevoInicial):
        if self.inicio.dpi is  None:
            self.inicio = NuevoInicial
            self.fin = NuevoInicial
        elif self.inicio.siguiente is None:
            self.inicio.siguiente = NuevoInicial
            self.fin = NuevoInicial
        else:
            self.fin.siguiente = NuevoInicial
            self.fin = NuevoInicial


    def recorriendo(self):
        aux = self.inicio
        contcli=0
        while aux!=None:            
            print('-------cliente-----')
            print('DPI:',aux.dpi)
            print('Nombre:',aux.nombre)
            contcli+=1
            aux.transs.recorriendo()           
            print(' ')
            aux=aux.siguiente        
        print(contcli)
    

    def imprimirCliente(self):
        nodo=self.inicio
        while nodo!=None:            
            print('Nombre:',nodo.nombre)
            nodo=nodo.siguiente




    def primerCli(self):
        aux = self.inicio
        self.inicio=self.inicio.siguiente
        return aux

   
        



