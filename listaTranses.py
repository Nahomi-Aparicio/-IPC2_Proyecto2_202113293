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

       

    def imprimir(self):        
        aux = self.inicio
        cadena=""        
        while True:           
            if aux.idTra is not None:              
                cadena += "ID"+aux.idTra+ "\n " +"Nombre"+ aux.nombretra+ "\n " +"tiempo Atencion"+ aux.TiempoTra+ "\n " 
                if aux.siguiente is not None:
                    aux = aux.siguiente
                    cadena+="\n"
                    self.cadena=cadena
                else:
                    break
            else:
                break
        
    def recorriendo(self):
        aux = self.inicio
        while aux!=None:            
            print('------transaccion------')
            print('ID:',aux.idTra)
            print('Nombre:',aux.nombretra)
            print('tiempo Atencion:',aux.TiempoTra)
            print(' ')
           
            aux=aux.siguiente
        
    
   
           
