def partie_entiere(x) :
    """float->int
    hyothese x>=0
    Retourne la partie entière de x"""

    #int n
    n=0
    while (n<=x and x<(n+1)) == False :
           n=n+1
    return n

assert partie_entiere(0.66)==0
assert partie_entiere(2.2)==2
assert partie_entiere(3)==3
