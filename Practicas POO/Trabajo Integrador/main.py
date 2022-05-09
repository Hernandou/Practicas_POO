from classListCam import ListCam
from classListMedicaments import ListMedicaments


if __name__ == '__main__':
    
    a = ListCam()
    b = ListMedicaments()
    
    nyaPac = input('>>  -Ingrese NOMBRE Y APELLIDO del Paciente: ')
    a.alta(nyaPac)
    id = a.buscarNomb(nyaPac)
    b.buscarID(id)
    
    diag = input('>> -Ingrese DIAGNOSTICO: ')
    a.Listado(diag)
    
    
    
    
    
    
    
    