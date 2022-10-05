
from xml.dom import minidom as MD

from Escritorio import Escritorio
from ListaSimpEscritorio import ListaSimpleEscritorio
from listaSimpleEmpresa import  listaSimpleEmpreza
from Empresa import Empreza
from puntoA import PuntoAtencion



from listasimpleInicial import listaSimpleInicial
from listaEscritorioInicial import escritorioActivo

from Escritorio import Escritorio
Emp=listaSimpleEmpreza()
ini=listaSimpleInicial(Emp)


class Menu:
    def __init__(self):
        self.root=None
        self.root2=None
        self.cont1=0
       
        

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
                self.nombre=input('escriba nombre de la empreza si existe: ')                    
                Emp.buscarEmpresaByNombre(nombri=self.nombre)                   
                #Emp.mostri_trans()
                self.ID=Emp.lasEmpresas()
                self.pu=Emp.lospuntos()
                self.TEs=Emp.getotroEs()
                
                    
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
                Emp.creadando_Empreza()
                pass
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
                #falta mucho :c
                ides1=Emp.lasEmpresas()
                idpu2=Emp.lospuntos()                
                ini.optEs(ides1,idpu2,self.TEs,nom=self.nombre)
                
            elif elegir==2:
                self.cont1=1
                ini.ActivarEs(p=self.ID,oo=self.pu,cont2=self.cont1)
                
            elif elegir==3:                             
                Emp.opteniendotodosEs(emp=self.ID,jo=self.pu)
                ini.ultimoEs(idpu=self.ID,ide=self.pu)
                
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
    def leyendo(self):
        self.root ="prueba1.xml"
        #self.root =filedialog.askopenfilename(title= "Abrir Archivo", filetypes=(("Xml","*.xml"),("Todos los archivos","*.*")))
        if self.root != "":
            return self.root
        return None

  
                               
                               
    
Menu().Menu()

        