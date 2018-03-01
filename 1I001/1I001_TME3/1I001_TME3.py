def somme_impairs_inf(n):
    """ int->int
    retourne la somme des entiers impairs inferieurs ou égaux à n."""
    #s: int
    s=0
    #i: int
    i=1
    while i<=n:
        s=s+i
        i=i+2
    return s
#jeu de tests:
assert somme_impairs_inf(1)==1
assert somme_impairs_inf(2)==1
assert somme_impairs_inf(5)==9

def somme_premiers_impairs(n):
    """ int-> int
    retourne la somme des n premiers impairs ."""
    #s: int
    s=0
    #i:int
    i=1
    while i<=n:
        s=s+(i*2-1)
        i=i+1
    return s
#jeu de tests:
assert somme_premiers_impairs(1)==1
assert somme_premiers_impairs(2)==4
assert somme_premiers_impairs(3)==9
assert somme_premiers_impairs(4)==16

def fibonacci(n) :
    """int->int
    hypothèse : n>=0
    calcule la somme des n premiers termes de la suite de Fibonacci telle que f0=0; f1=1; fn= F(n-2)+f(n-2)"""
    #int F, i, e, Fmoins1, Fmoins2
    i=2
    D=0
    Fmoins2=0
    Fmoins1=1
    F=0
    if n==0 :
        return 0
    if n==1 :
        return 1
    else :
        while i<=n :
            F=Fmoins1+Fmoins2
            Fmoins2=Fmoins1
            Fmoins1=F
            i=i+1
        return F
assert fibonacci(2)==1
assert fibonacci(0)==0
assert fibonacci(3)==2
assert fibonacci(8)==21

def fibo_diff(k):
    """int->int
    hypothèse : k>=0
    Retourne le k-ième terme de la suite Dk=Fk/F(k-1)"""
    e=0
    while e<=k :
        D=(fibonacci(k)/fibonacci(k-1))
        e=e+1
    return D

assert fibo_diff(5)==1.6666666666666667
assert fibo_diff(10)==1.6176470588235294
assert fibo_diff(41)==1.618033988749895

import math

def fibo_approx(n):
    """ int-> float
    hypothese: n>=0
    retourne les éléments approchés de la suite de Fibonacci."""
    #n_or: float
    n_or=( 1+math.sqrt(5))/2
    return (n_or**n)/math.sqrt(5)
#jeu de tests:
assert fibo_approx(5)==4.959674775249769
assert fibonacci(5)==5
assert fibo_approx(10)==55.00363612324743


    
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
