from classCama import Cama
import numpy as np
import csv

class ListCam:
    
    def __init__(self):
        self.__cam = np.empty(30, dtype = Cama)
        
        file = open('/Users/hernan/Desktop/UNSJ/Segundo Año/P O O/Practicas POO/Trabajo Integrador/camas.csv')
        reader = csv.reader(file, delimiter = ';')
    
        i = 0        
        for fila in reader:

            cma = Cama(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6])
            self.__cam[i]= cma
            i += 1
    
    def test(self):
        
        nuevaCama = Cama(1,202,True,'Eren Jaeger', 'Fimosis','20-4-22')
        self.__cam[29] = nuevaCama
        
        
    def buscarNomb(self,nya):
        
        i = 0
        band = False
        while(i < len(self.__cam) and (not band)):
            
            if(self.__cam[i].getNombre() == nya):
                
                band = True
                id = self.__cam[i].getIDC()
                print(self.__cam[i])
                return(id)                
            i+=1
            
        if(i >= len(self.__cam)):
            
            print('Paciente NO encontrado')
        
    
    def alta(self,nomb):
        
        i = 0
        band = False
        while(i < len(self.__cam) and not band):
            
            if(self.__cam[i]):
            
                if(self.__cam[i].getNombre() == nomb):
                
                    self.__cam[i].setAlta()
                    band = True
            
            i+=1
                
        if(i>= len(self.__cam)):
            print('>> -Paciente NO encontrado')
            
            
    def Listado(self,diag):
                
        for paciente in self.__cam:
            
            if(paciente != None):
                
                    if(paciente.getEstado() == True):
                        
                        if(paciente.getDiagnostico() == diag):
                                                
                            print(paciente)
                
            
        
        
    
            


    

        
            
        
        