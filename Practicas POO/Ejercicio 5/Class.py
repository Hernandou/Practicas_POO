
class PlanAhorro:

    __CodigoPlan = 0
    __Modelo = ''
    __VersionVehiculo = 0
    __ValorVehiculo = 0
    __CantCuotas = 0

    def __init__(self, codigo,modelo,versionVehiculo,ValorVehiculo,CantCuotas,CantCuotasPagas):
        if (((type(codigo) == int) and (type(modelo) == str) and (type(versionVehiculo) == str) and (type(ValorVehiculo) == int) and (type(CantCuotas) == int) and (type(CantCuotasPagas) == int))):
            
            self.__CodigoPlan = codigo
            self.__Modelo = modelo
            self.__VersionVehiculo = versionVehiculo 
            self.__ValorVehiculo = ValorVehiculo
            self.__CantCuotas = CantCuotas
            self.__CantCuotasPagas = CantCuotasPagas

    
    def getCodigoPlan(self):
        return(self.__CodigoPlan)

    def getModelo(self):
        return(self.__Modelo)

    def getVersion(self):
        return(self.__VersionVehiculo)

    def setValorVehiculo(self,valor):
        self.__ValorVehiculo = valor
    
    def getValor(self):
        return(self.__ValorVehiculo)
    
    def getCuotas(self):
        return(self.__CantCuotas)
    
    def getCantCuotasPagas(self):
        return(self.__CantCuotasPagas)



    def __str__(self):

        return('>> Codigo: {}\n>> Modelo: \n>>Version del Vehiculo: {}\n>> Valor del Vehiculo: {}\n>> Cant de cuotas {}'.format(self.__CodigoPlan,self.__Modelo,self.__VersionVehiculo,self.__ValorVehiculo,self.__CantCuotas))