from Galletas import *
from ListadoGalletas import menu


if __name__ == "__main__":

    list = []
    cent = True

    while(cent == True):

        op = menu()

        if(op == 1):

            huev = int(input("      Ingrese cantidad de HUEVOS: "))
            azucar =  float(input("      Ingrese cantidad de AZUCAR EN GRAMOS:  "))
            harina =  float(input("      Ingrese cantidad de HARINA EN GRAMOS: "))
            chocolate = float(input("      Ingrese CHOCOLATE EN GRAMOS: "))

            choc = GalletaChocolate(huev,azucar,harina,chocolate)

            list.append(choc)
            opc = input("\n   ¿Desea ver los INGREDIENTES totales de la galleta seleccionada? (SI/NO): ")
                
            if(opc == 'SI'):

                print(choc)

        elif(op == 2):


            huev = int(input("      Ingrese cantidad de HUEVOS: "))
            azucar =  float(input("      Ingrese cantidad de AZUCAR EN GRAMOS:  "))
            harina =  float(input("      Ingrese cantidad de HARINA EN GRAMOS: "))
            chips = float(input("      Ingrese CHIPS EN GRAMOS: "))

            chps = GalletaChips(huev,azucar,harina,chips)
                
            list.append(chps)
            opc = input("\n   ¿Desea ver los INGREDIENTES totales de la galleta seleccionada? (SI/NO): ")
                
            if(opc == 'SI'):

                print(chps)

            print()

        elif(op == 3):


            huev = int(input("      Ingrese cantidad de HUEVOS: "))
            azucar =  float(input("      Ingrese cantidad de AZUCAR EN GRAMOS:  "))
            harina =  float(input("      Ingrese cantidad de HARINA EN GRAMOS: "))
            vainilla = float(input("      Ingrese ESCENCIA/VAINILLA EN ML: "))

            vnl = GalletaVainilla(huev,azucar,harina,vainilla)
                
            list.append(vnl) 
            opc = input("\n   ¿Desea ver los INGREDIENTES totales de la galleta seleccionada? (SI/NO): ")

   
            if(opc == 'SI'):

                print(vnl)

        elif(op == 4):


            huev = int(input("      Ingrese cantidad de HUEVOS: "))
            azucar =  float(input("      Ingrese cantidad de AZUCAR EN GRAMOS:  "))
            harina =  float(input("      Ingrese cantidad de HARINA EN GRAMOS: "))
            coco = float(input("      Ingrese cantidad de COCO EN GRAMOS: "))
            coc = GalletaCoco(huev,azucar,harina,coco)

            list.append(coc) 
            opc = input("\n   ¿Desea ver los INGREDIENTES totales de la galleta seleccionada? (SI/NO): ")
    
            if(opc == 'SI'):

                print(coc)
                
        elif(op == 5):
            
            
            huev = int(input("      Ingrese cantidad de HUEVOS: "))
            azucar =  float(input("      Ingrese cantidad de AZUCAR EN GRAMOS:  "))
            harina =  float(input("      Ingrese cantidad de HARINA EN GRAMOS: "))
            arroz = float(input("      Ingrese cantidad de ARROZ EN GRAMOS: "))
            arz = GalletaArroz(huev,azucar,harina,arroz)
                
            list.append(arz)
            opc = input("\n   ¿Desea ver los INGREDIENTES totales de la galleta seleccionada? (SI/NO): ")
                
            if(opc == 'SI'):

                print(arz)
    
            cent = input("¿Desea crear una nueva galleta? (SI/NO): ")

        elif(op == 6):

            huev = int(input("      Ingrese cantidad de HUEVOS: "))
            azucar =  float(input("      Ingrese cantidad de AZUCAR EN GRAMOS:  "))
            harina =  float(input("      Ingrese cantidad de HARINA EN GRAMOS: "))
            arroz = (input("      Ingrese RELLENO (CHOCOLATE, DULCE DE LECHE, CREMA): "))
            rln = GalletaRellenas(huev,azucar,harina,arroz)
                
            list.append(rln)
            opc = input("\n   ¿Desea ver los INGREDIENTES totales de la galleta seleccionada? (SI/NO): ")
                
            if(opc == 'SI'):

                print(arz)
    
        cent = input("¿Desea crear una nueva galleta? (SI/NO): ")


        if(cent == 'SI'):

            cent = True
        
        elif(cent == 'NO'):

            cent = False

    print("\n       --- LISTA DE GALLETAS CREADAS ---")
    print(list)
