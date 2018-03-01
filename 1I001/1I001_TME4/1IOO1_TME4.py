def factorielle(n):
    """"int->int*hypothèse: n>=0
    Retourne le produit factoriel (n)!"""
    #k,f int
    k=1
    f=1
    while k<=n:

        f=f*k
        k=k+1
    return f

#Jeu de tests
assert factorielle(0)==1 #?????????????
assert factorielle(1)==1
assert factorielle(3)==6
assert factorielle(4)==24

#invariant de boucle : f = (k-1)!
# on aura à chaque tour de boucle f= k! et donc pour un n donné, on aura à la dernière boucle on aura f = k!, or à cette dernière boucle k=n donc on aura bien f=n!
# variant de boucle : n+1-k
#à la fin k=n+1 donc n+1-k=n+1-(n+1)=0



def decalage(c,d):
    """int*int->int
        c>=0
        Retourne la valeur d'un chiffre c entre 0 et 9 avec un décalage d (retourne n entre 0 et 9 décalé de d unités)"""
    #int n
    return (c+d)%10
    
assert decalage(0,2)==2
assert decalage(9,2)==1
assert decalage(8,2)==0
assert decalage(9,3)==2

def encodage(c,d):
    """int*int->int
        Retourne un réel c avec un décalage d pour chacun de ses chiffres le composant (retourne n entre 0 et 9 décalé de d unités pour chaque chiffre le composant)"""
    if c<=0 and c>=9:
        return (c+d)%10
    else :
        while dizaine*10<=c:
            dizaine=dizaine+1
        dizaine=dizaine-1
        unité=c-dizaine*10
        dizaine_d=(dizaine+d)%10
        unite_d=(unite+d)%10
        return dizaine_d*10+unite_d*1
assert encodage(84,2)==1062










































