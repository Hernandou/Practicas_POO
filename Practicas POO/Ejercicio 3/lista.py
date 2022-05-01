from clase import Registro
import csv
class CList:

    def __init__(self):

        self.__matriz = []
        file = open('datos.csv')
        reader = csv.reader(file, delimiter = ',')

        for dias in range(31):

            self.__matriz.append([])

            for horas in range(24):

                self.__matriz[dias].insert(horas,None)

        for fila in reader:
        
            obj = Registro(fila[2],fila[3],fila[4])    
            dia = int(fila[0])-1
            hora = int(fila[1])-1
            self.__matriz[dia].insert(hora,obj)

    def MostrarMatriz(self):

        for fila in self.__matriz:
            for valor in fila:
                print("\t", valor, end=" ")
        print()

    def Temperatura(self):
                     
        min = 99999
        max = 0
        day1 = 0
        hora1 = 0
        day = 0
        hora = 0
        for i in range(31):

            for j in range(24):

                if(self.__matriz[i][j] != None):

                    if(self.__matriz[i][j].getTemperatura() <= min):
                        min = self.__matriz[i][j].getTemperatura()
                        day = i
                        hora = j
                
                    if(self.__matriz[i][j].getTemperatura() >= max):
                        max = self.__matriz[i][j].getTemperatura()
                        day1 = i
                        hora1 = j
    
        print('>> La Minima Temperatura registrada en el Día {} - {}Hs es de: {}°'.format(day,hora,min))
        print('>> La Maxima Temperatura registrada en el Día {} - {}Hs es de: {}°'.format(day1,hora1,max))
        print('\n')
                               
    def Humedad(self):
                     
        min = 99999
        max = 0
        day1 = 0
        hora1 = 0
        day = 0
        hora = 0
        for i in range(31):

            for j in range(24):

                if(self.__matriz[i][j] != None):
                    if(self.__matriz[i][j].getHumedad() <= min):
                        min = self.__matriz[i][j].getHumedad()
                        day= i
                        hora = j

                    elif(self.__matriz[i][j].getHumedad() <= max):
                        max = self.__matriz[i][j].getHumedad()
                        day1 = i
                        hora1 = j
                        
        print('>> La Minima Humedad registrada en el Día {} - {}Hs es de: {}% '.format(day,hora,min))
        print('>> La Maxima Humedad registrada en el Día {} - {}Hs es de: {}% '.format(day1,hora1,max))
        print('\n')                   

    def Presion(self):
                     
        min = 99999
        max = 0
        day1 = 0
        hora1 = 0
        day = 0
        hora = 0

        for i in range(31):
            for j in range(24):
                if(self.__matriz[i][j] != None):
                    if(self.__matriz[i][j].getPresion() <= min):
                        min = self.__matriz[i][j].getPresion()
                        day = i
                        hora = j

                    elif(self.__matriz[i][j].getPresion() >= max):

                        max =  self.__matriz[i][j].getPresion()
                        day1 = i
                        hora1 = j

        print('>> La Minima Presion registrada en el Día {} - {}Hs es de: {}hPa '.format(day,hora,min))
        print('>> La Maxima Presion registrada en el Día {} - {}Hs es de: {}hPa '.format(day1,hora1,max))

    def TempMensual(self):

        temperaturas = 0
        i=0
        for i in range(24):

            for j in range(31):

                if(self.__matriz[j][i] != None):

                    temperaturas += self.__matriz[j][i].getTemperatura()

        print('La temperatura promedio por dia es: {}'.format(temperaturas/24))
        

    def ListadoValores(self,dia):
    
        if (dia <= 31 and dia > 0):
            print('Hora {}\t            Temperatura\t           Humedad\t           Presion'.format(0))

            for horas in range(24):

                if (self.__matriz[dia][horas] != None):
                    print('>> -Temperatura: {}°\t>> -Humedad: {}%\t>> -Presion: {}hPa'.format(self.__matriz[dia][horas].getTemperatura(),self.__matriz[dia][horas].getHumedad(),self.__matriz[dia][horas].getPresion()))
        else:

            print('Dia ingresado NO VALIDO')