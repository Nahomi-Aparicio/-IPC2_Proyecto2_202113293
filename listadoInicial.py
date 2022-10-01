from listaEscritorioInicial import escritoriosActivos
from listaCliente import listaSimpleClientes

class Inicial:
    def __init__(self, id=None, IdEmpreza=None,idPunto=None):
        self.id = id
        self.IdEmpreza = IdEmpreza
        self.idPunto = idPunto
        self.InicialES=escritoriosActivos()
        self.clientes=listaSimpleClientes()
        self.siguiente=None

    def getIdEmpreza(self):
        return self.IdEmpreza


       