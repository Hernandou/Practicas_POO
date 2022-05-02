
class Email:

    def __init__(self,idC,dominio,tipoDominio,passw):

        self.__idC = idC
        self.__dominio = dominio
        self.__tipoDominio = tipoDominio
        self.__passw = passw


    def getDominio(self):

        return(self.__dominio)

    def modifPass(self):


        a = 1
        while(a != 0):

            __ContrVieja = int(input('>> Ingrese Password actual: '))

            if (__ContrVieja == self.__passw):

             __nuevPass = int(input('>> Ingrese nueva Passwonrd: '))
             self.__passw = __nuevPass
             a = 0
            else:

                print('-- La Password ingresada es incorrecta\n')

    
    def crearCuenta(self):

        __passw = int(input('>> Ingrese password de usuario: '))

        if(__passw == self.__passw):

            print('-- Password Correcta\n')

        else:

            print('-- Password Incorrecta')

    def CrearCorreo(self,correo):

        cadena = correo.split('@')
        self.__idC = cadena[0]
        cadena = cadena[1].split('.')
        self.__dominio = cadena[0]
        self.__tipoDominio = cadena[-1]

    def BuscarRepetidos(self,identif,correo):

        if(identif == correo):

            print('El correo esta duplicado')


    def __str__(self):
        return('\nNueva instancia de correo creada: \n>> -ID: {} \n>> -Dominio: {}\n>> -Tipo de Dominio: {}\n'.format(self.__idC,self.__dominio,self.__tipoDominio))
        