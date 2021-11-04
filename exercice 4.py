"""suite de fibonacci"""
#defin fonction
def serie_fib(k):
#les conditions d'arrete
    if k==0:
        return 0
    elif k==1:
        return 1
    else :
        return serie_fib(k-1) + serie_fib(k-2)
x=int(input("entre le nombre de la suite : "))
print(serie_fib(x))