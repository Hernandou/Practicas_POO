class ViajeroFrecuente():

    def __init__(self,num_viajero,DNI,nombre,millas_acum):

        self.__num = num_viajero
        self.__DNI = DNI
        self.__nombre = nombre
        self.__millasAcum = int(millas_acum)


    def getID(self):

        return(self.__num)
    

    def  cantidadTotalMillas(self):

        return(self.__millasAcum)

    def acumularMillas(self, millas):

        self.__millasAcum += millas
        return(self.__millasAcum)

    def canjearMillas(self,millas):

        if(self.__millasAcum >= millas):

            self.__millasAcum -= millas
            return(self.__millasAcum)
        
        elif(self.__millasAcum < millas):

            print('Las millas ingresadas exceden las millas actuales del viajero')

