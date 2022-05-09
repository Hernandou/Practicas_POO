from classMenu import Menu


if __name__ == '__main__':
    
    mnu = Menu()
    band = False
    
            
    list1 = []
    num = int(input(('>> -Ingrese la cantidad de COMPONENTES del CONJUNTO 1: ')))
        
    for i in range(num):
            
        cmp = int(input('   >> Ingrese componente numero {}: '.format(i+1)))
        list1.append(cmp)
        
    list1.sort()    
    list2 = []
        
    num = int(input(('\n>> -Ingrese la cantidad de COMPONENTES del CONJUNTO 2: ')))
                
    for i in range(num):
            
        cmp = int(input('   >> Ingrese componente numero {}: '.format(i+1)))
        list2.append(cmp)        

    list2.sort()
    
    
    while(not band):
        
        print('''
    
        ------ Menu Opciones ------
        
        1) Funcion A (Suma de CONJUNTOS)
        2) Funcion B (Diferencia de CONJUNTOS)
        3) Funcion C (Comparador de CONJUNTOS)
        4) Salir
              
              
              ''')
        
        ans = str(input('>> -Ingrese Opcion: '))
        
        
        mnu.GestOpc(ans,list1,list2)
        
        if(ans == 4):
            band = True
    
    
 
    
    