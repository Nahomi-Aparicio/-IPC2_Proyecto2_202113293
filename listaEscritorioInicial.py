from Escritorio import Escritorio

class escritorioActivo:
    def __init__(self, idEscritorio=None):
        self.idEscritorio = idEscritorio       
        self.siguiente=None

    def getId(self):
        return self.idEscritorio
    def setId(self, idEscritorio):
        self.idEscritorio = idEscritorio

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
            aux.idEscritorio
            aux=aux.siguiente
            
    
    def ultimoNodo(self):
        aux = self.inicio       
        while aux.siguiente != None:            
            aux = aux.siguiente
                              
        return aux
    
    def elimini(self,key):
        aux = self.inicio
        temp=None
        
        while aux and aux.idEscritorio!= key: 
            temp=aux           
            aux = aux.siguiente
        if temp is None:
            self.inicio=aux.siguiente
        elif aux.siguiente is None:
            temp.siguiente=None

    def imprimir_lista(self):
        aux = self.inicio
        print('------Escritorio Activo-----')
        while aux!=None:
            
            print('idEscritorio:',aux.idEscritorio) 
            aux=aux.siguiente
        print('\n')

    def siexiste(self,id2):
        son_diferentes=0
        aux = self.inicio
        
        print(id2)
        while aux!=None:            
            for i in aux.idEscritorio:                
                for j in id2:
                    if i==j:
                       son_diferentes=1
                       break
                    
            aux=aux.siguiente
        if son_diferentes==0:
            print(son_diferentes)
            self.Agregar(escritorioActivo(id2))
            print('se agrego escritorio')
        else:
            print('escritorio ya existe')
            
            
            
                
            
            
                
            
        

            