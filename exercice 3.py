#defin fonction
def somme(n):
    #condition d'arrete
    if n==0:
        return n
    else:
        return n+somme(n-1)
m=int(input("veulliez saisir un nombre :"))
#caalling fonction
print("la somme est",somme(m))