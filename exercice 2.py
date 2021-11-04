#defin fonction
def convertir(n):
    nb=0
    #une boucle pour stocker la nombre binaire inverser
    while n !=0:
         k=n%2
         nb=nb*10+k
         n=n//2
    k=0
    #boucle pour trouver le vrai nombre binaire
    while nb!=0 :
        k=k*10+nb%10
        nb=nb//10
    return k
num=int(input("donner le nombre :"))
#calling the fonction
print(convertir(num))