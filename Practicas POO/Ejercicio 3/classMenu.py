from lista import CList
from clase import Registro
class Menu:

    __Switch = None


    def __init__(self):

        self.__Switch = {
            '1': self.opc1,
            '2': self.opc2,
            '3': self.opc3,
            '4':self.opc4   
        }


    def getSwitcher(self):

        return self.__Switch

    def GestOpc(self,opc):

        func = (self.__Switch.get(opc,lambda : print('Opcion no valida ')))
        func()
       

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
    


