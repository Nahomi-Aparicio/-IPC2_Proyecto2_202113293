class Escritorio:
    def __init__(self,ied=None,identificacionEs=None,encargadoEs=None):
        self.ied=ied
        self.identificacionEs=identificacionEs
        self.encargadoEs=encargadoEs
        self.siguiente=None


    def getId(self):
        return self.ied

    def getIdentificacionEs(self):
        return self.identificacionEs

    def getEncargadoEs(self):
        return self.encargadoEs

    def  setId(self,ied):
        self.ied=ied

    def setIdentificacionEs(self,identificacionEs):
        self.identificacionEs=identificacionEs

    def setEncargadoEs(self,encargadoEs):
        self.encargadoEs=encargadoEs

    
        
