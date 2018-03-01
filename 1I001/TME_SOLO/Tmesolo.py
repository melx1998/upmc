# Complétez les fonctions suivantes
# Testez-les avec des jeux de tests pertinents

def produit_entiers_liste(L):
    """ list(int) -> int

        Retourne le produit des éléments de la liste L

        Retourne 1 si la liste est vide. """
    #int res, e
    res=1 #le resultat du produit
    if L==[]:
        return 1
    else :
        for e in L:
            res=res*e
    return res

#Jeu de tests
assert produit_entiers_liste([])==1
assert produit_entiers_liste([1, 2, 3])==6
assert produit_entiers_liste([0, 2, 3])==0
            
            
    

    
def est_premier(n):
    """ int -> bool

        Hypothèse: n >= 1

        Retourne True ssi n est premier

        L'entier 1 est considéré premier."""
    #int i
    if n==1:
        return True
    else :
        for i in range(2, n):
            if n%i==0:
                return False
        return True

#Jeu de tests
assert est_premier(1)==True
assert est_premier(7)==True
assert est_premier(12)==False

    
    
def liste_premiers_plus_petits_ou_egaux(n):
    """ int -> list(int)

        Hypothèse: n >= 1

        Retourne la liste des entiers premiers plus petits ou égaux à n.

        La liste est ordonnée de manière décroissante, p.ex. pour n = 17,
        on obtient la liste [17, 13, 11, 7, 5, 3, 2, 1].

        L'entier 1 est considéré premier et figure dans la liste.

        Pour n = 1, retourne [1].

        La fonction est basée sur la fonction est_premier.

    """
    #list[int] res
    #int i
    res=[] #la liste des nombres premiers
    i=n #le compteur
    while i>=1:
        if i==1:
            res.append(i)
        elif est_premier(i)==True:
            res.append(i)
        i=i-1
    return res

assert liste_premiers_plus_petits_ou_egaux(17)==[17, 13, 11, 7, 5, 3, 2, 1]
assert liste_premiers_plus_petits_ou_egaux(1)==[1]
    

    
def decomposition_facteurs_premiers(n):
    """ int -> list(int)

        Hypothèse n >= 0

        Retourne une liste d'entiers premiers tel que leur
        produit est égal à n.

        L'entier 1 ne figure pas parmi les entiers de la liste retournée,
        sauf pour n = 1.

        Pour n = 0, retourne la liste [0]. Pour n = 1, retourne la liste [1].
    
        La fonction est basée sur la fonction 
        liste_premiers_plus_petits_ou_egaux."""
    #list[int] : res, L
    #int i
    res=[] #la liste des entiers premiers tel que leurproduit est égal à n
    L=liste_premiers_plus_petits_ou_egaux(n)
    i=n #compteur
    while i>=0 and produit_entiers_liste(res)!=n:
        if n%L[i]==0:
            res.append(L[i])
        i=i-1
    return res

assert decomposition_facteurs_premiers(17)==[17]
        
    
