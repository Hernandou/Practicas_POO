from classMedicamentos import Medicamentos
import csv

class ListMedicaments:

    __med = []
    
    def __init__(self):

        self.__med = []
        
        file = open('/Users/hernan/Desktop/UNSJ/Segundo Año/P O O/Practicas POO/Trabajo Integrador/medicamentos.csv')
        reader = csv.reader(file, delimiter = ';')
        
        for fila in reader:
            
            md = Medicamentos(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6])
            self.__med.append(md)
        
    def buscarID(self,id):
        
        i = 0
        band = False
        while(i < len(self.__med) and not band):

            if(self.__med[i].getIDC() == int(id)):
                band = True
                print('\n>> {}/{}\t >> Presentacion: {}\t   >> Cantidad: {}\t   >> Precio: ${}'.format(self.__med[i].getMedicamentos(),self.__med[i].getMonodrug(),self.__med[i].getPresentacion(),self.__med[i].getCantidad(),self.__med[i].getPrecio()))

            i+=1
            
        if(i >= len(self.__med)):

            print('>> Paciente NO encontrado')
                
                
                




        
        
