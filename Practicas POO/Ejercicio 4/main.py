from Class import Ventana

if __name__ ==  '__main__':


    print('==== Ventana Inicio ====')
    ventanaInicio= Ventana('Inicio')
    ventanaInicio.Mostrar()

    print('Ventana: {} Alto: {} Ancho: {}'.format(ventanaInicio.getTitulo(),ventanaInicio.alto(),ventanaInicio.ancho()))
    print('==== Ventana Cargar ====')

    ventanaCargar= Ventana('Cargar',10,20)
    ventanaCargar.Mostrar()

    print('*** Mueve a la derecha ***')
    ventanaCargar.moverDerecha(10)
    ventanaCargar.Mostrar()

    print('*** Mueve a la izquierda ***')
    ventanaCargar.moverIzquierda(10)
    ventanaCargar.Mostrar()

    print('*** Bajar ***')
    ventanaCargar.bajar(10)
    ventanaCargar.Mostrar()

    print('==== Ventana Borrar ====')
    ventanaBorrar = Ventana('Borrar', 10,20,100,200)
    ventanaBorrar.Mostrar()

    print('*** Subir ***')
    ventanaBorrar.subir(5)   
    ventanaBorrar.Mostrar()

    print('*** Subir ***')
    ventanaBorrar.subir()
    ventanaBorrar.Mostrar()
    
    print('*** Bajar ***')
    ventanaBorrar.bajar()
    ventanaBorrar.Mostrar()
