import time
class Cama:
    
    __ID = 0
    __habitacion = 0
    __estado = False
    __NyAPac = ''
    __diagnostico = ''
    __f_Internacion = ''
    __f_Alta = None
    
    def __init__(self,ID,habitacion,estado,NyAPac,diagnostico,f_Internacion,f_Alta = None):
        
        self.__ID = ID
        self.__habitacion = habitacion
        self.__estado = estado
        self.__NyAPac = NyAPac
        self.__diagnostico = diagnostico
        self.__f_Internacion = f_Internacion
        self.__f_Alta = f_Alta
        
    def getIDC(self):
        return(self.__ID)
    
    def getNombre(self):
        return(self.__NyAPac)
    
    def getDiagnostico(self):
        return(self.__diagnostico)
    
    def getEstado(self):
        return(self.__estado)
    
    def getHabitacion(self):
        return(self.__habitacion)
    
    def setAlta(self):
        self.__f_Alta = time.strftime('%d/%m/%Y',time.localtime())    
        
        
    def __str__(self):
        
        return('-NyA Paciente: {}\t>> -ID Cama: {}\t>> -Habitacion: {}\n>> -Diagnostico: {}\t>> -Fecha Internacion: {}\n>> -Fecha Alta: {}\n'.format(self.__NyAPac,self.__ID,self.__habitacion,self.__diagnostico,self.__f_Internacion,self.__f_Alta))