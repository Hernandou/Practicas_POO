
class Email:

    def __init__(self,idC,dominio,tipoDominio,passw):

        self.__idC = idC
        self.__dominio = dominio
        self.__tipoDominio = tipoDominio
        self.__passw = passw


    def retornaEmail(self,ID,dominio,tipoDominio,password):
        
        print('el ID es: {}'.format(self.ID))




if __name__ == '__main__':

    ID = input('Ingrese ID: ')
    dom = input('Ingrese Dominio: ')
    tipoDom = input('Ingrese Tipo Dominio: ')
    password = int(input('Ingrese Password: '))


    Email(ID,dom,tipoDom,password)
    Email.retornaEmail(ID,dom,tipoDom,password)