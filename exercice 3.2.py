list=[11,45,8,11,23,45,83]
#creer une dictionnaire vide
nombres={}
for x in list:
    j=0
    for i in list:
        if x==i:
            j+=1
    #ajouter les nombres comme CLÉ et le nombre d'occurrence
    nombres[x]=j
print(nombres)