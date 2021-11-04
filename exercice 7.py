def inverser(chaine):
    rev=''
    for i in range(len(chaine)-1,-1,-1):
        rev=rev+chaine[i]
    return rev
str='python'
#calling the fonction
print(inverser(str))
