
from  Escritorio import Escritorio

class ListaSimpleEscritorio:
    def __init__(self):
        self.inicio = Escritorio()
        self.fin =  Escritorio()
        

    def Agregar(self, NuevoEscritorio):
        if self.inicio.ied is  None:
            self.inicio = NuevoEscritorio
            self.fin = NuevoEscritorio
        elif self.inicio.siguiente is None:
            self.inicio.siguiente = NuevoEscritorio
            self.fin = NuevoEscritorio
        else:
            self.fin.siguiente = NuevoEscritorio
            self.fin = NuevoEscritorio

    def imprimir(self):
        aux = self.inicio
        cadena=""
        while True:
            if aux.ied is not None:
                cadena += "("+aux.ied+ " " + aux.identificacionEs+ " " + aux.encargadoEs+ " " + ") "
                if aux.siguiente is not None:
                    aux = aux.siguiente
                    cadena+="->"
                else:
                    break
            else:
                break
        print(cadena)

    def rerorriendoEs(self):
        aux = self.inicio
        while aux!=None:
            print('-------escritorios--------')
            print('ID:',aux.ied)
            print('Identificacion:',aux.identificacionEs)
            print('Encargado:',aux.encargadoEs)
            print(" ")          

            aux=aux.siguiente
           