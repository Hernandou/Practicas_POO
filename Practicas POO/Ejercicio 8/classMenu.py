from unittest import result
from Class import Conjunto

class Menu:
    
    __Switch = {}
    def __init__(self):
        
        self.__Switch = {
            
                '1' : self.opc1,
                '2' : self.opc2,
                '3' : self.opc3,
                '4' : self.opc4
            
        }
        
    def GestOpc(self,opc,list1,list2):
        
        func = self.__Switch.get(opc, lambda: 'Opcion Incorrecta')
        if (opc == '1' or opc == '2' or  opc == '3'):
            func(list1,list2)
        else:
            func()
    
    def opc1(self,list1,list2):
                     
        obj1 = Conjunto(list1)
        obj2 = Conjunto(list2)
        addition = Conjunto.__add__(obj1,obj2)
        print('La UNION de los dos conjuntos es: {}'.format(addition))

    def opc2(self,list1,list2):
        
        obj1 = Conjunto(list1)
        obj2 = Conjunto(list2)
        substraccion = Conjunto.__sub__(obj1,obj2)
        print('La diferencia de CONJUNTOS es: {}'.format(substraccion))
        
        

    def opc3(self,list1,list2):
        
        obj1 = Conjunto(list1)
        obj2 = Conjunto(list2)
        
        result = obj1 == obj2

    def opc4(self):
        
        print('nashe')
        
        
        
        
        
        