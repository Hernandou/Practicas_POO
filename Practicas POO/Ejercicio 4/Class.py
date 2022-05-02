
class Ventana:

    __titulo = ''
    __XSupIzq = 0
    __YSupIzq = 0

    __XInfDerech = 500
    __YInfDerech = 500

    def __init__(self,titulo,XSupIzq = 1,YSupDerech = 1,XInfDerech = 1,YInfDerech = 1):

        if(type(titulo) == str and type(XSupIzq) == int and type(YSupDerech) and type(YSupDerech) == int and type(YInfDerech) == int):

            if((self.__XSupIzq < self.__XInfDerech) and (self.__XSupIzq < self.__YInfDerech)):
                self.__titulo = titulo

                self.__XSupIzq = XSupIzq
                self.__YSupIzq =YSupDerech

                self.__XInfDerech = XInfDerech
                self.__YInfDerech = YInfDerech

    def Mostrar(self):

        print('>> La Esquina Superior Izquierdo: ({},{}) \n>> La Esquina Inferior Derecha: ({},{})'.format(self.__XSupIzq,self.__YSupIzq,self.__XInfDerech,self.__XInfDerech))

    def getTitulo(self):
        return(self.__titulo)
    
    def alto(self):
        return(self.__YSupIzq - self.__YInfDerech)

    def ancho(self):
        return(self.__XInfDerech - self.__YSupIzq)
    
    def moverDerecha(self,num):
        
        if(self.__YInfDerech + num <= 500 and self.__XInfDerech+ num <= 500):

            self.__XInfDerech += num
            self.__XSupIzq += num

    def moverIzquierda(self,num):

        if(self.__YSupIzq + num >=0 and self.__YInfDerech + num >= 0):

            self.__YInfDerech += num
            self.__YSupIzq += num

    def bajar(self,num = 1):

        if(self.__YInfDerech + num >= 500):

            self.__YSupIzq += num
            self.__YInfDerech += num
           
    def subir(self,num = 1):

        if(self.__YSupIzq - num >= 0):

            self.__YSupIzq -= num
            self.__YInfDerech -= num