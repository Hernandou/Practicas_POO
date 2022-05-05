from Class import ViajeroFrecuente


if __name__ == '__main__':
    
    obj = ViajeroFrecuente(12,5423234,'Eren Jaeger',534537643)
    ans = int(input('>> -Ingrese cantidad de millas a comparar: '))
    

    if(obj == ans):
        
        print('Las millas ingresadas son iguales a las millas del Viajero frecuente: \n {}'.format(obj))
        
    num = int(input('>> Ingrese cantidad de millas a acumular: '))
    add = obj + num
    print('Las millas actuales del viajero son: {}'.format(add))
    ans2 = int(input('>> -Ingrese numero de Millas a canjear: '))
    sub = obj - ans2
    
    print('>> Las millas fueron Canjeadas EXITOSAMENTE, millas actuales: {}'.format(sub))
    
    
