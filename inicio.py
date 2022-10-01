from xml.dom import minidom as MD

from Escritorio import Escritorio
from listaSimpleEmpresa import  listaSimpleEmpreza
from Empresa import Empreza
from puntoA import PuntoAtencion


from listadoInicial import Inicial
from listasimpleInicial import listaSimpleInicial
from listaEscritorioInicial import escritorioActivo
from  listaCliente import ClientesNodo
from lista_inicialTranse import TranseNodo



Emp=listaSimpleEmpreza()
ini=listaSimpleInicial(Emp)
class Menu:
    def __init__(self):
        self.root=None
        self.root2=None
        

    def Menu(self):
         while True:
            print("")
            print("════════════════════════════════════════════════")
            print("║                                              ║")
            print("║               Menu principal:                ║")
            print("║                                              ║")
            print("════════════════════════════════════════════════")
            print("║ 1. Configuración de empresas :               ║")
            print("║ 2. Selección de empresa y punto de atención  ║")
            print("║ 3. Manejo de puntos de atención:             ║")           
            print("║ 4. salir:                                    ║")           
            print("════════════════════════════════════════════════")
            elegir= int(input('ingrese una opcion:'))
            if elegir==1:
                self.SeleccionEmpresaMenu()
                
            elif elegir==2:    
                                     
                    Emp.recorriendo()
                    nombre=input('escriba nombre de la empreza si existe')                    
                    Emp.buscarEmpresaByNombre(nombri=nombre)                   
                    #Emp.mostri_trans()
                    
            elif elegir==3:
                self.ManejoMenu()
            elif elegir ==4:
                break
            else:
                print('escriba una opcion valida')

    def SeleccionEmpresaMenu(self):
        while True:
            print("")
            print("══════════════════════════════════════════════════════")
            print("║                                                    ║")
            print("║      Menu Configuración de empresas                ║")
            print("║                                                    ║")
            print("══════════════════════════════════════════════════════")
            print("║ 1. Limpiar sistema:                                ║")
            print("║ 2. Cargar archivo de configuración del sistema:    ║")
            print("║ 3. Crear nueva empresa                             ║")           
            print("║ 4. Cargar archivo con configuración inicial        ║") 
            print("║ 5. Regresar al menu  inicial                       ║")                                                
            print("══════════════════════════════════════════════════════")
            elegir= int(input('ingrese una opcion:'))
            if elegir==1:
                Emp.limpiar()
                print('------------------------')
                print('| El sistema se limpio |')
                print('------------------------')
            elif elegir==2:
                Emp.leyendo()
                Emp.Configsis()
                
                               
            elif elegir==3:
                self.creadando_Empreza()
            elif elegir ==4:
                self.leyendo2()
                ini.ConfiguInicial(root2=self.root2)
                ini.recorriendo() 
            elif elegir ==5:
                self.Menu()
            else:
                print('escriba una opcion valida')
    def ManejoMenu(self):
        while True:
            print("")
            print("════════════════════════════════════════════════")
            print("║                                              ║")
            print("║        Manejo de puntos de atención          ║")
            print("║                                              ║")
            print("════════════════════════════════════════════════")
            print("║ 1. Ver estado del punto de atención:         ║")
            print("║ 2. Activar escritorio de servicio:           ║")
            print("║ 3. Desactivar escritorio:                    ║")           
            print("║ 4. Atender cliente:                          ║") 
            print("║ 5. Solicitud de atención:                    ║")
            print("║ 6. Simular actividad del punto de atención:  ║")
            print("║ 7. Regresar al menu principal                ║")
            print("════════════════════════════════════════════════")
            elegir= int(input('ingrese una opcion:'))
            if elegir==1:
                pass
            elif elegir==2:
                pass
            elif elegir==3:
                pass
            elif elegir==4:
                pass
          
            elif elegir==5:                            
                j=Emp.lasEmpresas()
                k=Emp.lospuntos()
                ini.nuevoCliente(IdE=j,Idpu=k)
                
                ini.recorriendo()
            elif elegir==6:
                pass
            elif elegir ==7:
                break
            else:
                print('escriba una opcion valida')

    def leyendo2(self):
        self.root2 ="prueba2.xml"      
       
        #self.root2 = filedialog.askopenfilename(title= "Abrir Archivo", filetypes=(("Xml","*.xml"),("Todos los archivos","*.*")))
        if self.root2 != "":
            return self.root2        
        return None

                
    def creadando_Empreza(self):
        print("═════════════════════════")        
        print("║   Creando Empresa     ║")       
        print("═════════════════════════")
        idNuevo=input('ingrese ID de la empresa:')
        nombreNuevo=input('ingrese nombre de la empresa:')
        abrvnueva=input('ingrese abreviatura de la empresa:')
        
        nuevoEmpresa=Empreza(idNuevo,nombreNuevo,abrvnueva)        
        Emp.Agregar(nuevoEmpresa)

        print('-------creando punto de atencion-------')
        idAtencion=input('ingrese ID del punto de Atencion:')
        nombreAtencion=input('ingrese nombre del punto de Atencion:')
        direcAtencion=input('ingrese direccion del punto de Atencion:')
        NuevoAt=PuntoAtencion(idAtencion,nombreAtencion,direcAtencion)
        nuevoEmpresa.listaPuntoAtencion.Agregar(NuevoAt)

        print('-------creando escritorio-------')
        idEs=input('ingrese ID del Escritorio:')
        idEs2=input('ingrese la identificacion  del Escritorio:')
        EncargEs=input('ingrese encargado del Escritorio:')
        NuevoEscritorio=Escritorio(idEs,idEs2,EncargEs)
        NuevoAt.Escritorios.Agregar(NuevoEscritorio)        

    
        while True:
            print('---desea ingresar otro  Escritorio 1, sino 0 ---')
            ele2= int(input('ingrese una opcion:'))
            if ele2==1:
                print('-------creando escritorio-------')
                idEs=input('ingrese ID del Escritorio:')
                idEs2=input('ingrese la identificacion  del Escritorio:')
                EncargEs=input('ingrese encargado del Escritorio:')
                NuevoEscritorio=Escritorio(idEs,idEs2,EncargEs)
                NuevoAt.Escritorios.Agregar(NuevoEscritorio)
            elif ele2 ==0:
                break
            else:
                print('elija una opcion valida')

        while True:
            print('---desea ingresar otro  punto de atencion 1, sino 0 ---')
            ele= int(input('ingrese una opcion:'))
            if ele==1:

                print('-------creando punto de atencion-------')
                idAtencion=input('ingrese ID del punto de Atencion:')
                nombreAtencion=input('ingrese nombre del punto de Atencion:')
                direcAtencion=input('ingrese abreviatura del punto de Atencion:')
                NuevoAt=PuntoAtencion(idAtencion,nombreAtencion,direcAtencion)
                nuevoEmpresa.listaPuntoAtencion.Agregar(NuevoAt)

                print('-------creando escritorio-------')
                idEs=input('ingrese ID del Escritorio:')
                idEs2=input('ingrese la identificacion  del Escritorio:')
                EncargEs=input('ingrese encargado del Escritorio:')
                NuevoEscritorio=Escritorio(idEs,idEs2,EncargEs)
                NuevoAt.Escritorios.Agregar(NuevoEscritorio)
                while True:
                    print('---desea ingresar otro  Escritorio 1, sino 0 ---')
                    ele2= int(input('ingrese una opcion:'))
                    if ele2==1:
                        print('-------creando escritorio-------')
                        idEs=input('ingrese ID del Escritorio:')
                        idEs2=input('ingrese la identificacion  del Escritorio:')
                        EncargEs=input('ingrese encargado del Escritorio:')
                        NuevoEscritorio=Escritorio(idEs,idEs2,EncargEs)
                        NuevoAt.Escritorios.Agregar(NuevoEscritorio)
                    elif ele2 ==0:
                        break
                    else:
                        print('elija una opcion valida')

            elif ele ==0:
                break
            else:
                print('elija una opcion valida')

        print('------------------------')
        print('|   Empreza creada     |')
        print('------------------------')
        Emp.recorriendo()

    def ConfiguInicial(self):
        
        xml2=MD .parse(self.root2)
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
            ini.Agregar(nuevoInicio)

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
       
Menu().Menu()

"""def Configsis(self):
        xmldoc = MD.parse(self.root)
        ruta= xmldoc.documentElement
        emprezas= ruta.getElementsByTagName("empresa")
        
        for empreza in emprezas:
            #print('.........................................')
            id_empreza= empreza.getAttribute("id")
            nombre= empreza.getElementsByTagName("nombre")[0].firstChild.data
            abreviando= empreza.getElementsByTagName("abreviatura")[0].firstChild.data
            
            puntosAtencion= empreza.getElementsByTagName("puntoAtencion")
            ListaTranses= empreza.getElementsByTagName("transaccion")
            NuevoEmprez=Empreza(id_empreza,nombre,abreviando)            
            Emp.Agregar(NuevoEmprez)
            

            for puntoAtencio in puntosAtencion:
                idAtencion= puntoAtencio.getAttribute("id")
                nombreAtencion= puntoAtencio.getElementsByTagName("nombre")[0].firstChild.data
                direccionAtencion= puntoAtencio.getElementsByTagName("direccion")[0].firstChild.data
                listaEscritorios= puntoAtencio.getElementsByTagName("escritorio")
                NuevoPuntoAtencion=PuntoAtencion(idAtencion,nombreAtencion,direccionAtencion)
                NuevoEmprez.listaPuntoAtencion.Agregar(NuevoPuntoAtencion)
                # NuevoEmprez.listaPuntoAtencion.impri()
                for escritorio in listaEscritorios:
                    idEscritorio= escritorio.getAttribute("id")
                    idEscrit= escritorio.getElementsByTagName("identificacion")[0].firstChild.data
                    encargadoEscritorio= escritorio.getElementsByTagName("encargado")[0].firstChild.data
                    NuevoEscritorio=Escritorio(idEscritorio,idEscrit,encargadoEscritorio)
                    NuevoPuntoAtencion.Escritorios.Agregar(NuevoEscritorio)



            for transaccion in ListaTranses:
                idTran= transaccion.getAttribute("id")
                nombreTran= transaccion.getElementsByTagName("nombre")[0].firstChild.data
                tiempoTran= transaccion.getElementsByTagName("tiempoAtencion")[0].firstChild.data
                NuevaTransaccion=Transes(idTran,nombreTran,tiempoTran)
                NuevoEmprez.listaTrans.Agregar(NuevaTransaccion)
        print('------------------------')
        print('|   Archivo Cargado    |')
        print('------------------------')"""