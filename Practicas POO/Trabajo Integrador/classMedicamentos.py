
class Medicamentos:
    
    __IDC = 0
    __IDMed = 0
    __nombCom = ''
    __monodrug = ''
    __presentacion = ''
    __cantAplic = 0
    __precioTot = 0
    
    def __init__(self,IDC,IDMed,nombCom,monodrug,presentacion,cantAplic,precioTot):
            
        self.__IDC = int(IDC)
        self.__IDMed = int(IDMed)
        self.__nombCom = nombCom
        self.__monodrug = monodrug
        self.__presentacion = presentacion
        self.__cantAplic = cantAplic
        self.__precioTot = precioTot
        
        
    def getIDC(self):
        return(self.__IDC)
    
    def getMedicamentos(self):
        return(self.__nombCom)
    
    def getMonodrug(self):
        return(self.__monodrug)
    
    def getPresentacion(self):
        return(self.__presentacion)
    
    def getCantidad(self):
        return(self.__cantAplic)
    
    def getPrecio(self):
        return(self.__precioTot)
    

        
    
    
    def __str__(self):
        
        return('\n>> ID Cama: {}\n>> ID Medicamento: {}\n>> ID Nombre Comercial: {}\n>> Monodroga: {}\n>> Presentacion: {}\n>> Cantidad Aplicada: {}\n>> Precio Total: ${}'.format(self.__IDC,self.__IDMed,self.__nombCom,self.__monodrug,self.__presentacion,self.__cantAplic,self.__precioTot))