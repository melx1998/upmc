import math
def aire_disque(r):
    """ Number ->number
    hypothèse r>=0
    Retourne l'aire d'un disque de rayon r"""
    return math.pi*(r**2)
assert aire_disque(0)==0
assert aire_disque(1)==math.pi
assert aire_disque(2)==math.pi*4

def aire_couronne(r2,r1):
    """Number**2->Number
    hypothèse: r1<=r2
    retourne l'aire de la couronne de rayon intérieur r1 et de rayon extérieur r2"""
    return ((math.pi*(r2**2))-(math.pi*(r1**2)))
assert aire_couronne(0,0)==0
assert aire_couronne(1,0)==math.pi
assert aire_couronne(1,1)==0
