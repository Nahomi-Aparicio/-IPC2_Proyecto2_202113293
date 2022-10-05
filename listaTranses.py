from transes import Transes

class listaSimpleTranses:
    def __init__(self):
        self.inicio = Transes()
        self.fin =  Transes()
        

    def Agregar(self, NuevoEmpreza):
        if self.inicio.idTra is  None:
            self.inicio = NuevoEmpreza
            self.fin = NuevoEmpreza
        elif self.inicio.siguiente is None:
            self.inicio.siguiente = NuevoEmpreza
            self.fin = NuevoEmpreza
        else:
            self.fin.siguiente = NuevoEmpreza
            self.fin = NuevoEmpreza

    def recorriendo(self):
        aux = self.inicio
        while aux!=None:            
            print('------transacciones de la empreza------')
            print('ID:',aux.idTra)
            print('Nombre:',aux.nombretra)
            print('tiempo Atencion:',aux.TiempoTra)
            print(' ')           
            aux=aux.siguiente
        
            
    def tiempo(self):
        aux = self.inicio
        tiempo=0
        while aux!=None:            
            tiempo=tiempo+int(aux.TiempoTra)
            aux=aux.siguiente
        print(tiempo) 
    
    
        
    
   
           
