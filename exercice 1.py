#defin the first fonction
#pour calculer le factoriel d'un nombre

def factoriel(k):
    #condition d'arrete
    if k==0:
        return 1
    else:
        return k*factoriel(k-1)

#defin second fonction
#calculer la somme
def somme():
    s=0
    n= int(input("donner le nombre :"))
    for i in range(1,n+1):
        s = s + factoriel(i)/i
    return s
#calling the second fonction
print("la somme de serie est :",somme())
