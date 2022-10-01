

from xml.dom import minidom as MD
from listadoInicial import Inicial

from listaEscritorioInicial import escritorioActivo
from  listaCliente import ClientesNodo
from lista_inicialTranse import TranseNodo


from listaSimpleEmpresa import  listaSimpleEmpreza


class listaSimpleInicial:   
    
    def __init__(self,listaEmpresa):
        self.inicio = Inicial()
        self.fin =  Inicial()
        self.idemp=listaEmpresa

    def ConfiguInicial(self,root2):
        
        xml2=MD .parse(root2)
        rutaConfi=xml2.documentElement
        configIni= rutaConfi.getElementsByTagName("configInicial")
        
        for config in configIni:
            print('.........................................')
            id_config= config.getAttribute("id")
            idEmpresa= config.getAttribute("idEmpresa")
            idPunto= config.getAttribute("idPunto")
            escritori=config.getElementsByTagName("escritorio")
            listadoClientes= config.getElementsByTagName("cliente")
            nuevoInicio=Inicial(id_config,idEmpresa,idPunto)
            self.Agregar(nuevoInicio)

            #print("Configuracion Inicial: ", id_config, idEmpresa, idPunto)
            for escritorio in escritori:
                idEscritorio= escritorio.getAttribute("idEscritorio")
                #print("Escritorio: ", idEscritorio)
                nuevoEscritorioI=escritorioActivo(idEscritorio)
                nuevoInicio.InicialES.Agregar(nuevoEscritorioI)


            for listado in listadoClientes:
                idCliente= listado.getAttribute("dpi")
                nombreCliente= listado.getElementsByTagName("nombre")[0].firstChild.data
                listadoTransacciones= listado.getElementsByTagName("transaccion")
                nuevolistado=ClientesNodo(idCliente,nombreCliente)
                nuevoInicio.clientes.Agregar(nuevolistado)
                
                
                #print("Cliente: ", idCliente, nombreCliente)
                for transaccion in listadoTransacciones:
                    idTransaccion= transaccion.getAttribute("idTransaccion")
                    cantidTran= transaccion.getAttribute("cantidad")
                    nuevotranss=TranseNodo(idTransaccion,cantidTran)
                    nuevolistado.transs.Agregar(nuevotranss)

        print('------------------------')
        print('|   Archivo Cargado    |')
        print('------------------------')    
       

    def Agregar(self, NuevoInicial):
        if self.inicio.id is  None:
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
            print('════════════listadoInicial════════════')
            print('ID:',aux.id)
            print('idEmpresa:',aux.IdEmpreza)
            print('idPunto:',aux.idPunto)
            print(' ')
            aux.InicialES.recorriendo()
            print(' ')
            aux.clientes.recorriendo()
            print(' ')  
            aux=aux.siguiente
        
    def nuevoCliente(self,IdE,Idpu):
        aux = self.inicio 
        while aux!=None:
            if IdE== aux.IdEmpreza and Idpu==aux.idPunto: 
                                
                print('---------------------------------------')
                print('| ingrese sus datos para la solicitud |')
                print('---------------------------------------')
                self.nuevoDpi=input('Ingrese su DPI: ')
                self.nuevoNombre=input('Ingrese su Nombre: ') 
                if aux.IdEmpreza is None:
                    print('no hay empreza')                
                else:
                    NuevoCli=ClientesNodo(self.nuevoDpi,self.nuevoNombre)
                    aux.clientes.Agregar(NuevoCli)                                       
                    while True:
                        self.idemp.mostri_trans(x=IdE)
                        deseo=input('Desea agregar una transaccion? (s/n): ')
                        if deseo=='s':                                    
                            self.a=input('Ingrese el id de la transaccion: ')
                            self.b=input('Ingrese la cantidad: ')
                            NuevoCli.transs.Agregar(TranseNodo(self.a,self.b))                            
                        elif deseo=='n':
                            break
                        else:
                            print('---------------------------------------')
                            print('| opcion no valida                    |')
                            print('---------------------------------------')                  
                    
                aux=aux.siguiente
                print('---------------------------------------')
                print('| se a agregado una nueva solicitud   |')
                print('---------------------------------------')
            else:
               break

    def mostrarEs(self):
        aux = self.inicio
        while aux!=None:
            aux.InicialES.recorriendo()            
            aux=aux.siguiente
        

   

            


    
        

   