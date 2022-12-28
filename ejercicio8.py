def potencia(a,b):    
    if b==1:        
        return a    
    else:        
        return potencia(a,b-1)*a
print(potencia(2,3))