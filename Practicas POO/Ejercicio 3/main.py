from clase import Registro
from lista import CList
from classMenu import Menu
import csv


if __name__ == '__main__':

    band = False

    while not band:

        print('>> --- Menu ---')
        print('>> 1: Mostrar Matriz')
        print('>> 2: Minimo y Maximo de variables Metereologicas')
        print('>> 3: Temperatura Mensual')
        print('>> 4: Listado de valores')
        print('>> 5: Salir')
        opc = str(input('>> - Ingrese Numero de opcion: '))
        mnu = Menu()
        mnu.GestOpc(opc)
        if(opc == '5'):
            band = True