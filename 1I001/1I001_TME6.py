#Ex 6.2

def max_liste(L):
    """list[int]->int
    hypothèse: L n'est pas la liste vide
    Retourne le plus grand élément de la liste L passée en argument"""
    #int e, max
    max=L[0] #maximum initialisé à L[0]
    for e in L:
        if e>max:
            max=e
    return max

#Jeu de tests
assert max_liste([3, 7, 9, 5.2, 0.9, 8.999, 5])==9
assert max_liste([0, 0, 0, 0])==0

def nb_occurences(L, x):
    """liste[int]*float->int
    hypothèse
    Retourne le nombre d'occurences de l'élément x dans la liste L"""
    #int e, c
    c=0 #compteur initialisé à 0
    for e in L:
        if e==x:
            c=c+1
    return c

#Jeu de tests
assert nb_occurences([3, 7, 9, 5.4, 9, 8.999, 0, 90], 9)==2
assert nb_occurences([7, 7, 0, 7, 5.4, 9, 7, 90, 0.0002, 7], 7)==5

def nb_max(L):
    """list->int
    hypothese : L != []
    Retourne le nombre d'occurences du maximum de la liste"""
    #int e, c
    c=0 #compteur initialisé à 0    
    for e in L:
        if e==max_liste(L):
            c=c+1
    return c

assert nb_max([3, 7, 9, 5.4, 8.9, 9, 8.999, 5])==2
assert nb_max([-2, -1, -5, -3, -1, -4, -1])==3
assert nb_max([0, 0, 0, 0])==4

#Ex 6.9
def jonction(L,c):
    """ list[str]*str-> str
    hypothese: len(c)==1"""
    if len(L)==0:
        return ""
    #chaine:str
    chaine=L[0]
    #s:str
    for s in L[1:len(L)]:
        chaine=chaine+c+s
    return chaine
#jeu de tests
assert jonction(['un','deux','trois','quatre'], '.')=='un.deux.trois.quatre'
assert jonction([], '+')==''

def separation(s,c):
    """ str*str-> list[str]
    hypothese: len(c)==1
    Retourne la chaine s séparée du caractère c sans le caractère c"""
    #res:list[str]
    res=[]
    #debut, fin:int
    debut=0
    fin=0
    #ch:str
    for ch in s:
        if ch==c:
            if fin>debut:
                res.append(s[debut:fin])
                debut= fin+1
                fin=debut
        else:
            fin=fin+1
    if fin>debut:
           res.append(s[debut:fin])
    return res

assert separation('un.deux.trois.quatre','.')==["un","deux","trois","quatre"]
assert separation('les mots de cette phrase',' ')==["les", "mots", 'de', 'cette', "phrase"]

#Ex 6.8
def entrelacement(L1,L2):
    """list**2->list
    hypothèse: L1 et L2 sont de même type et de même longueur
    Retourne un entrelacement des 2 listes (en intercalant 1 élément sur 2 de chaque liste)"""
    #str L 
    L=[] #la liste entrelacée
    for e in range(len(L1)):
        L.append(L1[e])
        L.append(L2[e])
    return L

#Jeu de tests
assert entrelacement([1, 2, 3],[4, 5, 6])==[1, 4, 2, 5, 3, 6]
assert entrelacement(['p', 'l'],['o', 'o'])==['p', 'o', 'l', 'o']


def entrelacement_general(L1,L2):
    """list**2->list
    hypothèse : L1 et L2 de même type
    Retourne la liste en intercalant L1 et L2, et si l'une est plus longue que l'autre, on rajoutera ses éléments restants à la fin"""
    #int length, e, i 
    #str L
    L=[] #la liste entrelacée
    if len(L1)==len(L2):
        return entrelacement(L1,L2)
    if len(L1)<len(L2):
        return entrelacement(L1,L2[0:len(L1)])+L2[len(L1):]
    elif  len(L1)>len(L2):
        return entrelacement(L1[0:len(L2)],L2)+L1[len(L2):]

#Jeu de tests
assert entrelacement_general([1,2,3],[4,5,6])==[1, 4, 2, 5, 3, 6]
assert entrelacement_general([1,2,3],[4,5,6,8,8,8])==[1, 4, 2, 5, 3, 6, 8, 8, 8]

#Ex 6.7

def decoupage_simple(L,i,j):
    """ list[alpha]*int*int-> list[alpha]
    hypothese : i>=0 et j>=0
    retourne L[i:j]"""
    #res: list[alpha]
    res=[]
    #k: int
    for k in range(i,j):
        res.append(L[k])
    return res

# Jeu de tests
Comptine=['am','stram','gram','pic','pic','col','gram']
assert decoupage_simple(Comptine, 1, 3)== Comptine[1:3]
assert decoupage_simple(Comptine, 3, 4)== Comptine[3:4]

def decoupage_pas(L, i, j, p):
    """list[alpha]*int*int-> list[alpha]
    hypothese : i>=0 et j>=0, p>=1
    retourne L[i:j:p]"""
    #str L_pas
    #int n
    L_pas=[]
    n=0
    while i<=j:
         L_pas.append(L(i+p))
         i=i+p
    return L_pas

Comptine=['am','stram','gram','pic','pic','col','gram']
assert decoupage_pas(Comptine, 1, 5, 2)==Comptine[1:5:2]

        
