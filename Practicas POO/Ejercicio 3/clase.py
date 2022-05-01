class Registro:

    __temperatura = 0
    __humedad = 0
    __humedad = 0

    def __init__(self,temperatura,humedad,presion):
        
        self.__temperatura = temperatura
        self.__humedad = humedad
        self.__presion = presion

    def getTemperatura(self):
        return(int(self.__temperatura))

    def getHumedad(self):
        return(int(self.__humedad))

    def getPresion(self):
        return(int(self.__presion))

    def __str__(self):

        return('>> -Temperatura: {}\n>> -Humedad: {}\n>> -Presion: {}\n'.format(self.__temperatura,self.__humedad,self.__presion))




        
