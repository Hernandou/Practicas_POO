import csv
from Class import Email


if __name__ == '__main__':

    file = open('/Users/hernan/Desktop/U N S J/Segundo Año/P O O/Practicas POO/Ejercicio 1/DatosCorreos.csv')
    reader = csv.reader(file)

    list = []
    ID = str(input('>> Ingrese ID: '))
    dom = input('>> Ingrese Dominio: ')
    tipoDom = input('>> Ingrese Tipo Dominio: ')
    password = int(input('>> Ingrese Password: '))

    email_ = Email(ID,dom,tipoDom,password)
    list.append(email_)
    emailCreado = email_.retEmail()
  
    email_.modifPass()
    dominio = email_.getDominio()
    print('El dominio de su cuenta es: {}'.format(dominio))
    email_.crearCuenta()
    correo = input('Ingrese Correo: ')
    email_.CrearCorreo(correo)
    print(email_)

    for fila in reader:

        cadena = str(fila).split('@')
        idC = cadena[0]
        cadena = cadena[1].split('.')
        dominio = cadena[0]
        tipoDominio = cadena[-1]
        email_ = Email(idC,dominio,tipoDominio,0)
        list.append(email_)

    
    for correo in list:

        print(correo)
    

    ident = input('>> -Ingrese ID a buscar: ')
    for correo in list:

        email_.BuscarCadena(ident,str(correo))



    