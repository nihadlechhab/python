def compter(nombre,i=0):
    #Condition d'arrete
    if nombre==0:
        return i
    else:
        return compter(int(nombre/10),i+1)
number=int(input("donner le nombre :"))
print("les chiffres de nombre est :")
print(compter(number,0))