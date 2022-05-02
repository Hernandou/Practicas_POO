import csv
from Class import ViajeroFrecuente



#    def __str__(self):

#        return("\nInformacion Viajero: \n->> Numero: {}\n>> -DNI: {}\n>> -Nombre: {}\n>>  -Millas: {}".format(self.__num,self.__DNI,self.__nombre,self.__millasAcum))


def opc():

    print('------- Menu de Opciones -----')
    print('1) Consultar Cantidad de Millas')
    print('2) Acumular Millas')
    print('3) Canjear Millas')
    print('4) Mostrar almacenamiento en memoria')
    opci = int(input('>>> Ingrese Opciones: '))
    return(opci)

                    

if __name__ == '__main__':

    fins = 'n'
    line = []
    list = []
    file = open('/Users/hernan/Desktop/U N S J/Segundo Año/P O O/Practicas POO/Ejercicio 2/datos.csv')
    reader = csv.reader(file,delimiter = ',')

    for line in reader:

        i = 0
        band = True
        num_ = line[0]
        DNI = line[1]
        nombre = line[2]
        millas = line[3]

        viaj = ViajeroFrecuente(num_,DNI,nombre,millas)
        list.append(viaj)

    while(fins == 'n'):
        
        id = int(input('>> -Ingrese el numero del Viajero: '))

        while((band) and (len(list) > i)):

            if(int(list[i].getID()) == id):
                    
                band = False
            else:

              i += 1
                    

        if (band == True):

            print('No se encontro')
            
        else:

            print('>> Se encontro Viajero: ')
            op = opc()

            if (op == 1):

                print('La cantidad de millas Acumuladas: {}'.format(list[i].cantidadTotalMillas()))

            elif(op == 2):

                millas = int(input('>> -Ingrese la cantidad de millas: '))

                print('La nashe cantidad de millas Acumuladas: {}'.format(list[i].acumularlMillas(millas)))
            
            elif(op == 3):

                millas = int(input('>> -Ingrese la cantidad de millas: '))
                
                print('>> Canjear millas fue exitoso'.format(list[i].canjearMillas(millas)))

            elif(op == 4):

                print('La direccion de memoria de la lista cargada {}'.format(hex(id(list))))




        fins = input('¿Desea terminar?  (S = SI, N = NO): ')



    

        





    
    
    
        
