#Ex 3.4

def alphabet():
    """None->list[str]
    Retourne la liste des lettres de l'alphabet"""
    return [chr(i) for i in range (ord('a'), ord('z')+1)]

assert alphabet()==['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def est_voyelle(c):
    """str->Bool
    Retourne True si 'c' est une voyelle"""
    return (c=='a' or c=='e' or c=='i' or c=='o' or c=='u' or c=='y')
    
assert est_voyelle('e')== True
assert est_voyelle('a')== True

def voyelle():
    """None -> list[str]
    Retourne la liste des voyelles dans l'alphabet"""
    return [c for c in alphabet() if est_voyelle(c)]

assert voyelle()==['a','e','i','o','u','y']

def consonne():
    """None-> list[str]
Retourne la liste des consonnes dans l'alphabet"""
    return [c for c in alphabet() if not est_voyelle(c)]

assert consonne()==['b', 'c', 'd', 'f', 'g', 'h','j', 'k', 'l', 'm', 'n','p', 'q', 'r', 's', 't','v', 'w', 'x','z']

#Ex 3.5

def liste_caracteres(c):
    """str-> list[str] """
    return[c[i] for i in range (0,len(c))]

assert liste_caracteres('les carottes')==['l','e','s',' ','c','a','r','o','t','t','e','s']
assert liste_caracteres('')==[]

def chaine_de(L):
    """List[str]-> str
    Retourne la chaine de caractère correspondant à la liste L passée en paramètre"""
    #c : str
    res='' #la chaine de caracteres retournée
    for c in L:
        res=res+c
    return res

assert chaine_de(['l','e','s',' ','c','a','r','o','t','t','e','s'])=='les carottes'
assert chaine_de(liste_caracteres('les carottes'))=='les carottes'
assert chaine_de([])==''

def num_car(c):
    """str->int
    hypothèse c est une lettre  minusdcule
    Retourne la lettre c codée (0 pour 'a', etc)"""
    return ord(c)-ord('a')

assert num_car('a')==0
assert num_car('z')==25

def car_num(n):
    """int -> str
    hypothèse : n>=0 et n<=25
    Retourne le caractère correspondant à l'entier entrée en caractère selon le code instauré dans la fonction num_car"""
    return chr(n+ord('a'))
assert car_num(25)=='z'
assert car_num(0)=='a'

def rot13(c):
    if c==' ':
        return ' '
    return car_num((num_car(c)+13)%26)

assert rot13('a')=='n'

def codage_rot13(s):
    return chaine_de([rot13(c) for c in s])

assert codage_rot13('les carottes sont cuites')=='yrf pnebggrf fbag phvgrf'

#Ex 8.4

def liste_non_multiple(n,L):
    """ int*list[int]-> list[int]
    hypothese: n>0
    retourne la liste des elements de L qui ne sont pas multiples de n."""
    return[k for k in L if not k%n==0]

assert liste_non_multiple(7,[2,3,4,5,6,7,8,9,10])==[2,3,4,5,6,8,9,10]
assert liste_non_multiple(2,[2,3,4,5,6,7,8,9,10])==[3,5,7,9]

def eratosthene(n):
    L=[]
    for k in range (2, n+1):
        if n%k!=0:
            
           L.append(k)
    return L

assert eratosthene(10)==[2,3,5,7]





    

