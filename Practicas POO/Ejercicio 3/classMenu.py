from lista import CList
from clase import Registro
class Menu:

    __Switch = None

    # Switcher opciones (las vergas publicas son metodos)
    def __init__(self):

        self.__Switch = {
            '1': self.opc1,
            '2': self.opc2,
            '3': self.opc3,
            '4':self.opc4   
        }

    #es un get normalucho
    def getSwitcher(self):

        return self.__Switch

    def GestOpc(self,opc):

        func = (self.__Switch.get(opc,lambda : print('Opcion no valida ')))
        func()
       
    #la pija del switch
    def opc1(self):
        
        print('lol')
        a = CList()
        a.MostrarMatriz()
    
   
    def opc2(self):

        a = CList()
        a.Temperatura()
        a.Humedad()
        a.Presion()
        
    def opc3(self):
        a = CList()
        a.TempMensual()
    
    def opc4(self):
        a = CList()
        nro = int(input('>> -Ingrese numero de dia: '))
        a.ListadoValores(nro)
    


