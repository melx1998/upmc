import math
def volume_tetraedre(a,b,c,d,e,f):
    """Number**6->Number
    hypothee 4*(a**2)*(b**2)*(c**2)>(a**2)*(x**2)+(b**2)*(z**2)+(c**2)*(y**2)+x*y*z
    Retourne le volume d'un tétraèdre de côtés a,b,c,d,e,f"""
    #float p, q, r, x, y, z
    x=a**2+b**2-d**2
    y=b**2+c**2-e**2
    z=a**2+c**2-f**2
    p=4*(a**2)*(b**2)*(c**2)
    q=(a**2)*(x**2)+(b**2)*(z**2)+(c**2)*(y**2)
    r=x*y*z
    return (1/12)*math.sqrt(p-q+r)
#Jeu de tests
assert volume_tetraedre(0,0,0,0,0,0)==0
assert volume_tetraedre(1,1,1,1,1,1)==0.11785113019775792
assert volume_tetraedre(2,2,2,2,2,2)==0.9428090415820634
