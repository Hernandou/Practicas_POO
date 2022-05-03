from classMenu import Menu


if __name__ == '__main__':

    print('nashe')
    band = False
    while (not band):

        print(''' 
        
        --------- Menu ---------
        >> 1)   Metodo A 
        >> 2)   Metodo B
        >> 3)   Metodo C
        >> 4)   Salir
        
        ''')

        ans = str(input('>> -Ingrese Opcion: '))
        mnu = Menu()
        

        mnu.Gestopc(ans)

        if(ans == '4'):

            band = True
