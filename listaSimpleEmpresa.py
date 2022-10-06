from Empresa import Empreza
from Escritorio import Escritorio
from puntoA import PuntoAtencion
from transes import Transes
from xml.dom import minidom as MD
from tkinter import filedialog
class listaSimpleEmpreza:

    def __init__(self):
        self.inicio = Empreza()
        self.fin =  Empreza()
        
    def leyendo(self):
        #self.root ="prueba1.xml"
        self.root =filedialog.askopenfilename(title= "Abrir Archivo", filetypes=(("Xml","*.xml"),("Todos los archivos","*.*")))
        if self.root != "":
            return self.root
        return None

    def Configsis(self):
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
            self.Agregar(NuevoEmprez)
            

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
        print('------------------------')

    def Agregar(self, NuevoEmpreza):
        if self.inicio.id is  None:
            self.inicio = NuevoEmpreza
            self.fin = NuevoEmpreza
        elif self.inicio.siguiente is None:
            self.inicio.siguiente = NuevoEmpreza
            self.fin = NuevoEmpreza
        else:
            self.fin.siguiente = NuevoEmpreza
            self.fin = NuevoEmpreza
              
    def creadando_Empreza(self):
        print("═════════════════════════")        
        print("║   Creando Empresa     ║")       
        print("═════════════════════════")
        son_diferentes=0
        idNuevo=input('ingrese ID de la empresa:')
        aux=self.inicio
        while aux!=None:
            if idNuevo==aux.id:
                
                son_diferentes=1
            aux=aux.siguiente
        if son_diferentes==0:

            nombreNuevo=input('ingrese nombre de la empresa:')
            abrvnueva=input('ingrese abreviatura de la empresa:')
            
            
            nuevoEmpresa=Empreza(idNuevo,nombreNuevo,abrvnueva)

            self.Agregar(nuevoEmpresa)

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
            self.recorriendo()
        else:
            print('-----------------------------------')
            print('| ID ya existe, empreza existente |')
            print('|        Empreza no creada        |')
            print('-----------------------------------')
           
    def recorriendo(self):
        aux = self.inicio
        while aux!=None:            
            print('════════════Empresa════════════')
            print('ID:',aux.id)
            print('Nombre:',aux.nombre)
            print('Abreviacion:',aux.abrev)
            print(' ')
            aux.listaTrans.recorriendo()
            aux.listaPuntoAtencion.recorri()
            
            aux=aux.siguiente
            
    def buscarEmpresaByNombre(self, nombri):
        aux= self.inicio        
        while aux!=None:
            if nombri.lower()== aux.nombre.lower():
                print('----------------------------')
                print('| Se a elejido una empresa |')
                print('----------------------------')
                print('ID:',aux.id)
                print('Nombre:',aux.nombre)
                print('Abreviacion:',aux.abrev)
                print(' ')                
                aux.listaPuntoAtencion.recorri() 
                
                punti=input('Ingrese el ID del punto de atencion que desea buscar: ')                
                aux.listaPuntoAtencion.buscarPuntoNombre(puntito=punti)
                self.ContarES=aux.listaPuntoAtencion.getContarES()
                aux.listaTrans.tiempo()
                self.TiempoPromedio=aux.listaTrans.getPro()            
                aux.listaTrans.tiempo_MAX()
                self.TiempoMax=aux.listaTrans.getMax()

                aux.listaTrans.tiempo_MIN()
                self.TiempoMin=aux.listaTrans.getMin()
                self.idEmpresa=aux.id
                self.idPunto=punti
            aux=aux.siguiente 
            
    def Tpromedio(self):
        return self.TiempoPromedio 

    def getotroEs(self):
        return self.ContarES
   
    def limpiar(self):
            self.inicio = None
            self.fin =  None
 
    def lasEmpresas(self):
        return self.idEmpresa

    def lospuntos(self):
        return  self.idPunto

    def TMIN(self):
        return self.TiempoMin

    def TMAX(self):
        return self.TiempoMax

    def mostri_trans(self,x):
        aux=self.inicio 
               
        while aux!=None:
            
            if x==aux.id:
                aux.listaTrans.recorriendo()
            aux=aux.siguiente
           

    def buscaNombre(self,pi,k):
        aux= self.inicio        
        while aux!=None:
            if pi== aux.id:
                aux.listaPuntoAtencion.buscarNombre(p=k)
            aux=aux.siguiente 
      

    def opteniendotodosEs(self,emp,jo):
        aux= self.inicio 
              
        while aux!=None:
            if emp== aux.id:
                aux.listaPuntoAtencion.opteniendotodosEScri(p=jo)               
                a=aux.listaPuntoAtencion.getA()                
                self.a=a
            aux=aux.siguiente
            

    def getA(self):
        return self.a


    
#optener todoss los escritorios aqui

    def opteniendoEs(self,ed,pu):
        aux= self.inicio              
        while aux!=None:
            if ed== aux.id:
                aux.listaPuntoAtencion.opteniendotodosEScri(p=pu)               
                a=aux.listaPuntoAtencion.getA()                
                self.escri=a
            aux=aux.siguiente
            

    def getEscri(self):
        return self.escri




             
        
                
            








        
           

            
           

        
       



            
        
           
            
           

