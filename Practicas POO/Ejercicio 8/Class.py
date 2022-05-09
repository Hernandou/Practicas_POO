

class Conjunto:
    
    def __init__(self,list):
        
        self.__conjunto = list
    
    
    def __add__(self,other):
        
        list = []
        list = sorted(set(self.__conjunto + other.__conjunto))
        return(list)       
    
    def __sub__(self,other):

        list1 = set(self.__conjunto)
        list2 = set(other.__conjunto)
        resultado = sorted(set(list1 - list2))

    def __eq__(self,other):
        
        if(len(self.__conjunto) == len(other.__conjunto)):
            
            band = True
            i = 0
            
            while(((i< len(self.__conjunto) and band) == True)):
                j = 0
                
                while(j < len(other.__conjunto) and self.__conjunto[i] != other.__conjunto[j]):
                    j+=1

                if(j >= len(other.__conjunto)):
                    band= False
                
                i+=1
                
            if(band == False):
                print('>> -Los CONJUNTOS NO son iguales')
                
            else:   
                print('>> -Los CONJUNTOS SON IGUALES')
        else:
            print('>> -Los CONJUNTOS NO son iguales')
        
                        
                        
                
               
               
               
               
               
                

                    
                    
                    
                    
                    
                    


                    
                    
    
     


        

        
