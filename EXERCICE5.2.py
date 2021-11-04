l1=[47, 64, 69, 37, 76, 83, 95, 97]
dic={'Yassine':47, 'Imane':69, 'Mohammed':76, 'Abir':97}
#creer une liste vide
t=[]
#stocker les nombres qui ne sont pas dans le dic
for  i in l1:
     if i not in dic.values() :
        t.append(i)
#delete the tab's element from liste 1
for i in t:
    l1.remove(i)
print("la liste après la supprission : ",l1)