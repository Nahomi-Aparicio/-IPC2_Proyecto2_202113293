from  puntoA import PuntoAtencion
class ListaSimpleAtencion:
    def __init__(self):
        self.inicio = PuntoAtencion()
        self.fin =  PuntoAtencion()
       
    def Agregar(self, NuevoPuntoAtencion):
        if self.inicio.idA is  None:
            self.inicio = NuevoPuntoAtencion
            self.fin = NuevoPuntoAtencion
        elif self.inicio.siguiente is None:
            self.inicio.siguiente = NuevoPuntoAtencion
            self.fin = NuevoPuntoAtencion
        else:
            self.fin.siguiente = NuevoPuntoAtencion
            self.fin = NuevoPuntoAtencion

   

    def recorri (self):
        aux = self.inicio
        while aux!=None:
            print('----puntos de atencion-----')
            print('ID:',aux.idA)
            print('Nombre:',aux.nombre)
            print('Direccion:',aux.direccion)
           
            #print('----Escritorios-----')
            #aux.Escritorios.rerorriendoEs()
            print(' ')
            aux=aux.siguiente

    def buscarPuntoNombre(self,puntito):
        aux= self.inicio
        while aux!=None:                           
                if puntito== aux.idA:
                    print('---------------------------------------------')
                    print('| Se a elejido el punto de atencion empresa |')
                    print('---------------------------------------------')
                    print('ID:',aux.idA)
                    print('Nombre:',aux.nombre)
                    print('direcion:',aux.direccion)
                    aux.Escritorios.rerorriendoEs()
                    self.contarEsc=aux.Escritorios.getContarES()                    
                aux=aux.siguiente

    def getContarES(self):
        return self.contarEsc

    
                    
                

    def buscarNombre(self,p):
        aux= self.inicio
        while aux!=None: 
            if p== aux.idA:  
                a=aux.Escritorios.optener_ultimo().getId()
                print(a)
            aux=aux.siguiente
        return a


    def opteniendotodosEScri(self,p):
        aux = self.inicio
        while aux!=None:
            if p== aux.idA:                
                a=aux.Escritorios.ultimoNodo().getId()                
                self.a=a                             
            aux=aux.siguiente
        

    def getA(self):
        return self.a

  #optener los escritorios y todos los id 
    def opteniendoES(self,c):
        aux = self.inicio
        while aux!=None:
            if c== aux.idA:
                a=aux.Escritorios.optenerTodos().getId()
                self.co=a
            aux=aux.siguiente
        
    def getCo(self):
        return self.co