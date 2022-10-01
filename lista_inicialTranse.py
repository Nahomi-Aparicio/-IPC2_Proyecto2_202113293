class TranseNodo:
    def __init__(self, idTransaccion=None,cantidad=None):
        self.idTransaccion = idTransaccion   
        self.cantidad = cantidad    
        self.siguiente=None
        

class listaSimpleTransess:
    def __init__(self):
        self.inicio = TranseNodo()
        self.fin =  TranseNodo()
        

    def Agregar(self, NuevoInicial):
        if self.inicio.idTransaccion is  None:
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
        while aux!=None:            
            print('-----transaccion-----')
            print('idTransaccion:',aux.idTransaccion)
            print('cantidad:',aux.cantidad)            
            aux=aux.siguiente
    
    

