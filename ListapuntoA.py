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

    def impri(self):
        aux = self.inicio
        cadena=""
        while True:
            if aux.idA is not None:
                cadena += "("+aux.idA+ "\n" + aux.nombre+ "\n " + aux.direccion+ "\n " + ") "
                if aux.siguiente is not None:
                    aux = aux.siguiente
                    cadena+="\n"
                else:
                    break
            else:
                break
        print(cadena)

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
                    print('Abreviacion:',aux.direccion)
                    
                    aux=aux.siguiente
                    
                else:
                    break
