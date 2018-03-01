Grandes_Lignes={'Paris': {'Strasbourg', 'Dijon', 'Toulouse', 'Lille', 'Lyon', 'Bordeaux'}, 'Strasbourg': {'Paris', 'Dijon', 'Munchen'}, 'Munchen': {'Strasbourg'}, 'Dijon': {'Paris', 'Strasbourg', 'Lyon', 'Toulouse'}, 'Lyon': {'Paris', 'Dijon', 'Toulouse'}, 'Toulouse': {'Paris', 'Lyon', 'Dijon', 'Bordeaux'}, 'Bordeaux': {'Nantes', 'Paris'}, 'Nantes': {'Paris', 'Bordeaux', 'Quimper'}, 'Quimper': {'Nantes'}, 'Ajaccio': {'Bastia'}, 'Bastia': {'Ajaccio'}}

#Ex 10.5
def trajet_direct(carte,st1,st2):
    """ dict[str:str]*str*str->bool"""
    if st1 in carte and st2 in carte[st1]:
        return True
    return False
assert trajet_direct(Grandes_Lignes,'Paris','Bordeaux')==True

def ajout_station(st, corr, carte):
    """set[str]*str*str->dict[str: str]"""
    copie=dict()
    for e in carte:
        copie[e]=carte[e]
    copie[st]=corr #rajout de la ville + corresp
    for s in corr: #rajout de la ville en tant que corresp pr chacune des villes
        copie[s].add(st)
    return copie

Nouvelles_Lignes=ajout_station('Limoges', {'Paris', 'Toulouse', 'Bordeaux'}, Grandes_Lignes)
assert trajet_direct(Nouvelles_Lignes,'Limoges','Paris')==True

def stations_atteignables(carte, depart, k):
    """dict[str: str]*str*int->set[str]"""
    #0 correspondance : gare de départ. 1 correspondance: gares atteignables depuis la gare depart
    E1={depart}
    E2=set() #correspondances à E1
    for e in carte[depart]: #assignation des correspondances de E1 dans E2 (ensemble arrivée)
        E2.add(e)
    if k==0: #convention
        return E1
    for i in range(1, k):
        for s1 in E2: #e2->e1
            E1.add(s1)
        for s2 in E1: #(correspondances e2)->e2
            if s2 in carte:
                for s3 in carte[s2]:
                    E2.add(s3)
    return E2

#Jeu de tests
Grandes_Lignes={'Paris': {'Strasbourg', 'Dijon', 'Toulouse', 'Lille', 'Lyon', 'Bordeaux'}, 'Strasbourg': {'Paris', 'Dijon', 'Munchen'}, 'Munchen': {'Strasbourg'}, 'Dijon': {'Paris', 'Strasbourg', 'Lyon', 'Toulouse'}, 'Lyon': {'Paris', 'Dijon', 'Toulouse'}, 'Toulouse': {'Paris', 'Lyon', 'Dijon', 'Bordeaux'}, 'Bordeaux': {'Nantes', 'Paris'}, 'Nantes': {'Paris', 'Bordeaux', 'Quimper'}, 'Quimper': {'Nantes'}, 'Ajaccio': {'Bastia'}, 'Bastia': {'Ajaccio'}}
assert stations_atteignables(Grandes_Lignes, 'Paris', 0)=={'Paris'}
assert stations_atteignables(Grandes_Lignes, 'Paris', 1)=={'Strasbourg', 'Dijon', 'Toulouse', 'Lille', 'Lyon', 'Bordeaux'}
assert stations_atteignables(Grandes_Lignes, 'Dijon', 2)=={'Strasbourg', 'Dijon', 'Toulouse', 'Lille', 'Lyon', 'Bordeaux', 'Paris', 'Munchen'}




#Ex 10.4

LivresBD={'Les miserables':('Victor Hugo', 5), 'Les dernier des Mohicans':('James F. Cooper', 0), 'Un animal doue de raison':('Robert Merle', 6), 'Le grand Meaulnes':('Alain Fournier', 1), 'Notre-dame de Paris':('Victor Hugo', 4), 'Les comtemplations':('Victor Hugo', 0)}

def auteurs(Livres):
    """ dict[str:tuple[str,int]]->set[str]
    Retourne l'ensemble des noms d'auteurs de la base Livres"""
    return {nom for titre, (nom,nb_exemplaire) in Livres.items()}

assert auteurs(LivresBD)=={'Victor Hugo', 'James F. Cooper', 'Robert Merle', 'Alain Fournier'}


def titres_empruntable(Livres):
    """dict[str:(str, int)]->set[str]"""
    return {titre for titre,(nom,nb_exemplaire) in Livres.items() if nb_exemplaire>0}

assert titres_empruntable(LivresBD)=={'Les miserables','Un animal doue de raison','Le grand Meaulnes','Notre-dame de Paris'}

def titres_auteur(nom_auteur, Livres):
    """ str* dict[str:(str,int)]->set[str]"""
    return {titre for titre,(nom,nb_exemplaire) in Livres.items() if nom_auteur==nom}


assert titres_auteur('Victor Hugo', LivresBD)=={'Les comtemplations', 'Notre-dame de Paris', 'Les miserables'}




#Ex 10.3

def melements_list(L):
    """"list[str] ou dictionnaire ->set[str]"""
    return {c for c in L}

assert melements_list(['a', 'a', 'a', 'b', 'c', 'c'])=={'a', 'b', 'c'}

def melements_dict(D):
    """"list[str] ou dictionnaire ->set[str]"""
    return {c for c,freq in D.items() if freq>0}

assert melements_dict({'a':5, 'b':1, 'c':2, 'd':0})=={'a', 'b', 'c'}

def mdict_de_mlist(L):
    """L[str]->dict[str:int]"""
    D=dict() #le dictionnaire multi ensemble retourné 
    for c in L:
        if c in D:
            D[c]=D[c]+1
        else:
            D[c]=1
    return D

assert mdict_de_mlist(['a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c'])=={'a': 2, 'b': 4, 'c': 3}

def mlist_de_mdict_sans_comprehension(D):
    """dict[str: int]-> L"""
    L=[] #la liste multi-ensemble retournee
    for c in D:
        for i in range(D[c]):
            L.append(c)
    return L

assert mlist_de_mdict_sans_comprehension({'a': 2, 'b': 4, 'c': 3})==['a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c']
assert mlist_de_mdict_sans_comprehension({'a': 2, 'b': 4, 'c': 3, 'd': 0})==['a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c']


def mlist_de_mdict_avec_comprehension(D):
    """dict[str: int]-> L"""
    return [c for c in D for i in range(D[c])]

assert mlist_de_mdict_avec_comprehension({'a': 2, 'b': 4, 'c': 3})==['a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c']
assert mlist_de_mdict_avec_comprehension({'a': 2, 'b':4, 'c': 3, 'd': 0})==['a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c']

def minter_dict(D1,D2):
    """ dict[str:int]*dict[str:str]->dict[str:str]"""
    D3=dict()
    for lettre in D1:
        if lettre in D2:
            D3=min(D1[lettre],D2[lettre])
    return D3
assert mint_dict({'a': 2, 'b': 4, 'c': 3},{'a': 1, 'f':1, 'c': 9, 'd': 0})=={'a':1,'c':3}



            













