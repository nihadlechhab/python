list=[]
size=int(input("donner la size de liste"))
#remplir la liste principal
for i in range(size):
    n = int(input("le nombre"))
    list.append(n)
l1=[]
l2=[]
l3=[]
print(list)
#traiter les cas où l'indix apartient à quelle morceaux
for i in range(0,len(list)):
    if i<len(list)/3:
        l1.append(list[i])
    elif i>=2*len(list)/3:
        l3.append(list[i])
    else :
        l2.append(list[i])
#inverser les morceaux
l1.reverse()
l2.reverse()
l3.reverse()
#afficher les morceaux
print(l1,l2,l3)