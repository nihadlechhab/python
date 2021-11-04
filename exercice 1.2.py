l1=[3, 6, 9, 12, 15, 18, 21]
l2=[4, 8, 12, 16, 20, 24, 28]
l3=[]
# boucle pour tester les indexes de premier liste
for i in l1:
    a=l1.index(i)
    if a % 2 != 0:
       l3.append(i)
#boucle pour tester les indexes de dexième liste
for j in l2:
    b = l2.index(j)
    if b % 2 == 0:
        l3.append(j)
print ("nouvelle liste : ",l3)