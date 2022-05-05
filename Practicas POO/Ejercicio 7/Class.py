class ViajeroFrecuente:

    def __init__(self,num_viajero,DNI,nombre,millas_acum):

        self.__num = num_viajero
        self.__DNI = DNI
        self.__nombre = nombre
        self.__millasAcum = int(millas_acum)


    def __gt__(self,other):
        
        if (self.__millasAcum, other.__millasAcum):

            return(self.__millasAcum)
        else:

            return(other.__millasAcum)

    def __add__(self,other):
        return(self.__millasAcum + other)

    def __sub__(self,other):
        return(self.__millasAcum - other)
    
    def __eq__(self,other):
        
        if(self.__millasAcum == other):
            
            return(True)
        else:
            
            return(False)
  
    def __str__(self):

        return('\n>> ID: {} \n>> Nombre: {}\n>> DNI: {}\n>> Millas: {}\n'.format(self.__num,self.__nombre,self.__DNI,self.__millasAcum))
        

