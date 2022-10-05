import os
from lista_inicialTranse import listaSimpleTransess
from lista_inicialTranse import TranseNodo
class ClientesNodo:
    def __init__(self, dpi=None,nombre=None):
        self.dpi = dpi   
        self.nombre = nombre
        self.transs=listaSimpleTransess()   
        self.siguiente=None
        

class listaSimpleClientes:
    def __init__(self):
        self.inicio = ClientesNodo()
        self.fin =  ClientesNodo()
        

    def Agregar(self, NuevoInicial):
        if self.inicio.dpi is  None:
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
            print('-------cliente-----')
            print('DPI:',aux.dpi)
            print('Nombre:',aux.nombre)           
            aux.transs.recorriendo()           
            print(' ')
            aux=aux.siguiente        
        
    

    def imprimirCliente(self):
        nodo=self.inicio
        while nodo!=None:            
            print('Nombre:',nodo.nombre)
            nodo=nodo.siguiente


    def primerCli(self):
        aux = self.inicio
        self.inicio=self.inicio.siguiente
        return aux
    
    def mostrarclientes(self):
        
        text = 'cli[shape=plaintext ,label =<<TABLE><TR><TD>CLIENTES EN LA COLA</TD></TR>'
        aux = self.inicio
        while aux!=None:            
            
            text += '<TR><TD>'+'DPI:'+str(aux.dpi)+'  Nombre:'+str(aux.nombre)+'</TD></TR>'
        
            aux=aux.siguiente
        text += '</TABLE>>];\n'
       
        self.cli=text
        

    def getText(self):
        return self.cli

        
       



   
        



