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
        self.root ="prueba1.xml"
        #self.root =filedialog.askopenfilename(title= "Abrir Archivo", filetypes=(("Xml","*.xml"),("Todos los archivos","*.*")))
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

    def imprimir(self):        
        aux = self.inicio
        cadena=""        
        while True:           
            if aux.id is not None:              
                cadena += "("+aux.id+ "\n " + aux.nombre+ "\n " + aux.abrev+ "\n " + ") "
                if aux.siguiente is not None:
                    aux = aux.siguiente
                    cadena+="\n"
                else:
                    break
            else:
                break
        print(cadena)
        
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
                self.idEmpresa=aux.id
                self.idPunto=punti
                aux=aux.siguiente                
            else:
                break
     

    def limpiar(self):
            self.inicio = None
            self.fin =  None
 
    def lasEmpresas(self):
        return self.idEmpresa

    def lospuntos(self):
        return  self.idPunto

    def mostri_trans(self):
        aux=self.inicio
        while aux!=None:
            print('---estas son las transacciones posibles en la empreza')

            aux.listaTrans.recorriendo()
            aux=aux.siguiente
            break
        



             
        
                
            








        
           

            
           

        
       



            
        
           
            
           

