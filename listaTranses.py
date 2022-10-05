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
        cont=0
        while aux!=None:            
            tiempo=tiempo+int(aux.TiempoTra)
            cont=cont+1
            aux=aux.siguiente
        ti=(tiempo/cont)
        self.tiempoPro=ti

    def getPro(self):
        return self.tiempoPro


    
    def tiempo_MAX(self):
        aux = self.inicio
        tiempo=0
        tiempo=float(aux.TiempoTra)
        while aux!=None: 
            if float(aux.TiempoTra)>tiempo:
                tiempo=float(aux.TiempoTra) 
            aux=aux.siguiente
        self.tiempoMax=tiempo

    def getMax(self):
        
        return self.tiempoMax

    def tiempo_MIN(self):
        aux = self.inicio
        tiempo=0
        tiempo=float(aux.TiempoTra)
        while aux!=None: 
            if float(aux.TiempoTra)<tiempo:
                tiempo=float(aux.TiempoTra) 
            aux=aux.siguiente
        self.tiempoMin=tiempo
    
    def getMin(self):
        return self.tiempoMin
        
        
    


    
        
    
   
           
