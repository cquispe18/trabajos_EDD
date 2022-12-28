def sumarecursiva(a,b):    
    if b==0:        
        return a    
    else:        
        return sumarecursiva(a,b-1)+1
print(sumarecursiva(1,10))