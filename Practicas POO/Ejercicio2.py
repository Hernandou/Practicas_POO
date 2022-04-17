import csv

class ViajeroFrecuente():

    def __init__(self,num_viajero,DNI,nombre,millas_acum):

        self.__num = num_viajero
        self.__DNI = DNI
        self.__nombre = nombre
        self.__millas_acum = millas_acum


    def __str__(self):

        return(" - Numero: {} -DNI: {} -Nombre: {}  -Millas: {}".format(self.__num_viajero,self.__DNI,self.__nombre,self.__millas_acum))

    

def opc():

    print('------- Menu de Opciones -----')
    print('1) Consultar Cantidad de Millas')
    print('2) Acumular Millas')
    print('3) Canjear Millas')
    opci = int(input('>>> Ingrese Opciones: '))
    return(opci)

                     
    

if __name__ == '__main__':

    lista = []
    op = opc()
    line = []
    list = []
    file = open('alumnos.csv','r')
    reader = csv.reader(file,delimiter = ',')

    for line in reader:

        num_ = line[0]
        DNI = line[1]
        nombre = line[2]
        millas = line[3]

        viaj = ViajeroFrecuente(num_,DNI,nombre,millas)
        list.append(viaj)

    print(list[2])
    
        

        
        





    
    
    
        
