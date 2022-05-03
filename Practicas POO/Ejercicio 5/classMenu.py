from classLista import Lista

class Menu:

    __Switch = None
    
    def __init__(self):

        self.__Switch = {
            '1' : self.opc1,
            '2' : self.opc2,
            '3' : self.opc3,
        }

    def getSwitch(self):

        return(self.__Switch)

    def Gestopc(self,opc):

        func =self.__Switch.get(opc, lambda: print("Opción no válida"))
        func()

    def opc1(self):

        list = Lista()
        list.ActualizarValorPlan()

  
    def opc2(self):

        list = Lista()
        value = int(input('\n>> -Ingrese Valor: '))
        list.Valor(value)

    def opc3(self):

        list = Lista()
        list.MostrarMonto()

