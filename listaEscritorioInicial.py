class escritorioActivo:
    def __init__(self, idEscritorio=None):
        self.idEscritorio = idEscritorio       
        self.siguiente=None
        

class escritoriosActivos:
    def __init__(self):
        self.inicio = escritorioActivo()
        self.fin =  escritorioActivo()
        

    def Agregar(self, NuevoInicial):
        if self.inicio.idEscritorio is  None:
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
            print('------Escritorio Activo-----')
            print('idEscritorio:',aux.idEscritorio)  
            aux=aux.siguiente


            