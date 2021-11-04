set1={23, 42, 65, 57, 78, 83, 29}
set2={57, 83, 29, 67, 73, 43, 48}
t=[]
#stocker l'intersection dans un liste
for x in set1 :
    for y in set2 :
        if x==y :
            t.append(y)

print("l'interseection est :",set1.intersection(set2))
#supprimer les nombres intersectioner de les sets
for i in t:
    set1.remove(i)
print("la set1 aprés supprission : ",set1)