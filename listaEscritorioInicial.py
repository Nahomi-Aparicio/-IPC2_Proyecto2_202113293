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
        cotact=0
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
        cotact=0
        print('------Escritorio Activos-----')
        while aux!=None:
            cotact+=1
            print('idEscritorio:',aux.idEscritorio) 
            aux=aux.siguiente
        print('\n')
        self.contact=cotact
        
    def getContar(self):
        return self.contact

    def siexiste(self,id2):
        son_diferentes=0
        aux = self.inicio
        print(id2)
        while aux!=None:
                if id2==aux.idEscritorio:
                    print('holi')
                    son_diferentes=1
                    break
                
                aux=aux.siguiente
        if son_diferentes==0:            
            self.Agregar(escritorioActivo(id2))
            print('se agrego escritorio',id2)
        else:
            print('escritorio ya se encuentra activo')


#mostrar escrotorios
   

            