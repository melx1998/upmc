#Ex 9.4
def nb_ingredients(D,r):
    """ dict[str: set[str]]*str->int
    retourne le nombre d'ingredients d'une recette r à partir de D """
    return len(D[r])

Dessert={'gateau chocolat':{'chocolat','oeuf','farine','sucre','beurre'},'gateau yaourt':{'yaourt','oeuf','farine','sucre'}, 'crepes': {'oeuf','farine','lait'}, 'quatre-quarts':{'oeuf','farine','beurre','sucre'}, 'kouign amann':{'farine','beurre','sucre'}}

#Jeu de tests
assert nb_ingredients(Dessert, 'crepes')==3
assert nb_ingredients(Dessert, 'gateau yaourt')==4

def recette_avec(D, i):
    """dict[str: set[str]]*str->set[str]"""
    res=set()
    for e in D:
        for s in D[e]:
            if s==i:
                res.add(e)
    return res

assert recette_avec(Dessert, 'lait')=={'crepes'}

def tous_ingredients(D):
    """dict[str: set[str]]->set[str]"""
    res=set()
    for e in D:
        for s in D[e]:
            res.add(s)
    return res

assert tous_ingredients(Dessert)=={'beurre','chocolat','farine','lait','oeuf','sucre','yaourt'}

def table_ingredients(D):
    """dict[str: set[str]]->dict[str: set[str]]"""
    res={}
    for i in tous_ingredients(D):
        res[i]=recette_avec(D, i)
    return res

assert table_ingredients(Dessert)=={'lait':{'crepes'}, 'chocolat':{'gateau chocolat'}, 'beurre':{'gateau chocolat', 'kouign amann', 'quatre-quarts'}, 'yaourt':{'gateau yaourt'}, 'oeuf':{'crepes','gateau chocolat', 'gateau yaourt', 'quatre-quarts'}, 'farine':{'crepes', 'gateau chocolat', 'gateau yaourt', 'kouign amann', 'quatre-quarts'}, 'sucre':{'gateau chocolat', 'gateau yaourt', 'kouign amann', 'quatre-quarts'}}

def ingredient_principal(D):
    """dict[str: set[str]]->str"""
    res=''
    TABLE=table_ingredients(D)
    for e in TABLE:
        if len(TABLE[e])>=len(res):
            res=e
    return res

assert ingredient_principal(Dessert)=='farine'

def recettes_sans(D, i):
    """dict[str: set[str]]*str->set[str]"""
    allergie=table_ingredients(Dessert)[i]
    res={}
    for e in table_ingredients(D):
        if e!=i:
            for s in D[e]:
                if s==i:
                    R=False

        
    return res
assert recettes_sans(Dessert,'farine')=={}



















    
