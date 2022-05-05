import csv
from Class import ViajeroFrecuente


if __name__ == '__main__':

    obj1 = ViajeroFrecuente(14,4324234,'Chris Dennis',7236262338)
    obj2 = ViajeroFrecuente(4,33274744,'Marc Tomminson',72362638)

    print('>> El viajero con mayor cantidad de Millas: {}'.format(obj1 > obj2))
    print('\n>> Se han acumulado las Millas del viajero {}'.format(obj1 + 100000))
    print('\n>> Las millas fueron canjeadas (100 Millas), millas actuales:{}'.format(obj1 - 24535688))







        


    



