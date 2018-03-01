def somme_carres(n):
    """int->int
    hypothèse n>=0
    Retourne la somme des carrés des entiers de 0 à n"""
    #int S, i
    S=0 #somme des carrés initialisée à 0
    for i in range(0,n+1):
       S=S+i*i
    return S

assert somme_carres(5)==55

def produit_cube(m,n):
    """int*int->int
    hypothese: m>=0 and n>=0 m<n
    retourne le produit des cubes des entiers de m à n """
    #p: int, k
    p=1 #produit initialisé à 1
    for k in range(m,n):
        p=p*k*k*k
    return p
assert produit_cube(4,6)==8000
assert produit_cube(1,2)==1
assert produit_cube(3,5)==1728


#def ord(c):
    #"""str->int
    #hypothèse : len(c)=1
    #Retourne le numéro unicode du caractère c"""

def chiffre(c):
    """str->int
    hypothèse len(c)=1
    Retourne l'entier correspondant à un caractère représentant un chiffre donné en argument"""
    return (ord(c)-ord('0'))

assert chiffre('5')==5
assert chiffre('0')==0
assert chiffre('1')==1

def entier(nb):
    """ str-> int
    hypothèse: tous les caracteres de la chaine nb sont des chiffres
    retourne l'entier représenté par la chaine s""" 
    #res:int
    res=0 #l'entier représenté par la chaine s
    #c:str
    for c in nb:
        res=res*10
        res= res+chiffre(c)
    return res
assert entier('92')==92
assert entier('0425')==425
assert entier('0')==0


#def chr(n):
#   """int->str
#    hypothèse: n>=48
#   Retourne un caractère à partir de son numéro unicode n"""

def caractere(n):
    """int->str
    hypothèse: 0<=n<=9
    Retourne un caractère à partir de son numéro unicode n"""
    return chr(n+ord('0'))

assert caractere(9)=='9'

def chaine(n):
    """ int-> str
    hypothèse: n>=0
    retourne la chaine ch correspondant à l'entier naturel n """
    #ch: str
    ch='' #chaine de caractères correspondant à l'entier n
    #reste: int
    r=n #reste de la division de q//n
    while r>10:
        ch=caractere(r%10)+ch
        r=r//10
    return caractere(r)+ch
  
assert chaine(598)=='598'
assert chaine(8)=='8'
assert chaine(0)=='0'

def est_palindrome(s):
    """str->bool
    hypothèse: s n'est pas vide
    Retourne True si la chaine de caractères s est un palindromen False sinon."""
    #str inverse
    #int c
    inverse='' #la chaine s à l'envers
    for c in s:
        inverse=c+inverse
    return inverse==s

assert est_palindrome('aba')==True
assert est_palindrome('amma')==True
assert est_palindrome('etnon')==False

def miroir(s):
    """str->str
    hypothèse : s n'est pas vide
    Retourne un palindrome construit à partir de la chaine de caractere  s"""
    #str inverse
    #int c
    inverse='' #la chaine s à l'envers
    for c in s:
        inverse=c+inverse
    return s+inverse

assert miroir('abc')=='abccba'
assert miroir('amanaplanacanal')=='amanaplanacanallanacanalpanama'
assert miroir('do-re-mi-fa-sol')=='do-re-mi-fa-sollos-af-im-er-od'

def base_comp(base):
    """ str->str
    hypothèse: base {'A', 'T', 'C', 'G'}
    Retourne la base complémentaire"""
    if base=='A':
        return 'T'
    if base=='T':
        return 'A'
    if base=='G':
        return 'C'
    if base=='C':
        return 'G'
assert base_comp('A')=='T'
assert base_comp('C')=='G'
assert base_comp('G')=='C'
assert base_comp('T')=='A'

def brin_comp(s):
    """str->str
    hypothèse :base {'A', 'T', 'C', 'G'}
    Retourne le brin complémentaire du brain s"""
    #str compl
    #int c
    compl='' #brin complémentaire de s qui sera retourné
    for c in s:
        compl=compl+base_comp(c)
    return compl

assert brin_comp('ATCG')=='TAGC'
assert brin_comp('ATTGCCGTATGTATTGCGCT')=='TAACGGCATACATAACGCGA'
assert brin_comp('')==''

def test_comp(b1,b2):
    """str*str-> bool
    hypothèse : b1 et b2 sont construits depuis la base {'A', 'T', 'C', 'G'}
    Retourne True si b1 et b2 sont complémentaires, False sinon"""
    return brin_comp(b1)==b2

assert test_comp('','')==True
assert test_comp('','ATCG')==False
assert test_comp('ATCG','TAGC')==True

def test_sous_sequence(b1,b2):
    """ str*str-> bool
    hyp: b1,b2 sont des brins d'ADN
    Retourne True si la b1 est une sous-séquence de b2 (si b1 apparaît dans b2)"""
    #i: int
    for i in range(len(b2)+1):
        if b1==b2[i:i+len(b1)]:
            return True
    return False

assert test_sous_sequence('','')==True
assert test_sous_sequence('','ATCG')== True
assert test_sous_sequence('GC','TAAG')== False

def cherche_sans_sequence(b1,b2):
    """str*str-> int*spe type
    renvoie l'indice de b2 correspondant au début de b1 si b1 est une sous-sequence de b2 et ne renvoie rien sinon"""
    #int i
    for i in range(0, len(b2)+1):
        if b2[i: i+len(b1)]==b1:
            return i
    return None


assert cherche_sans_sequence('','')==0
assert cherche_sans_sequence('','ATCG')==0
assert cherche_sans_sequence('GC','TAGC')==2
assert cherche_sans_sequence('GC','TAAC')==None
