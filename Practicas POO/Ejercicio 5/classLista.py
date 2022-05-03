import csv
from Class import PlanAhorro
import time

class Lista:

    __lista = []

    def __init__(self):

        self.__lista = []

        file = open('/Users/hernan/Desktop/U N S J/Segundo Año/P O O/Practicas POO/Ejercicio 5/planes.csv')
        reader = csv.reader(file, delimiter = ';')

        for fila in reader:

            obj = PlanAhorro (int(fila[0]),str(fila[1]),str(fila[2]),int(fila[3]),int(fila[4]),int(fila[5]))
            self.__lista.append(obj)


    def ActualizarValorPlan(self):

        for i in range(len(self.__lista)):

            print('--- Auto: {}'.format(i+1))
            print('Codigo del Plan: {}'.format(self.__lista[i].getCodigoPlan()))
            print('Modelo del Vehiculo: {}'.format(self.__lista[i].getModelo()))
            print('Version del Vehiculo: {}'.format(self.__lista[i].getVersion()))
            ans = input('>> - ¿Desea actualizar el Valor de este Vehiculo? (SI/NO): ')

            if(ans == 'SI' or ans == 'si'):

                valor = int(input('>> -Ingrese Valor del Vehiculo a actualizar: '))
                self.__lista[i].setValorVehiculo(valor)
            
        
        for j in range(len(self.__lista)):

            print('>> -El valor del Vehiculo {} es: {}'.format(j+1,self.__lista[j].getValor()))

    def Valor(self,value):

        cuota = 0

        for i in range(len(self.__lista)):

            cuota = (self.__lista[i].getValor() / self.__lista[i].getCuotas()) * 0.10
            if (value <= cuota):
                
                print('Codigo del Plan: {}'.format(self.__lista[i].getCodigoPlan()))
                print('Modelo del Vehiculo: {}'.format(self.__lista[i].getModelo()))
                print('Version del Vehiculo: {}'.format(self.__lista[i].getVersion()))
    

    def MostrarMonto(self):

        cuota = 0

        for i in range(len(self.__lista)):
            print('\n')
            cuota = (self.__lista[i].getValor() / self.__lista[i].getCuotas()) + self.__lista[i].getValor() * 0.10
            importe = (self.__lista[i].getCantCuotasPagas() * cuota)
            print(self.__lista[i])
            print('\n>> -El importe que se deberia haber pagado para licitar este vehiculo es: ${}'.format(round(importe,2)))
            








            

        




    