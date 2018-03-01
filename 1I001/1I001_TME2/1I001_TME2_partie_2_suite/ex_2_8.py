def rectangle(x, y, l, h):
    """Number**4-> image
    hypothese : l>=L
    Affiche un  rectangle à partir de son point bas-gauche (x,y), sa longueur l et sa hauteur h"""
    triangle1=fill_triangle(0, 0, l, h, 0, h)
    triangle2=fill_triangle(0, 0, l, h, l, 0)
    return overlay(triangle1, triangle2)
show_image(rectangle(0, 0, 1, 0.5))
show_image(rectangle(-1, 1, 1.5, 0.3))

def tour(h, l, L):
    """Number**3-> image
    hypothèse : L>=l
    Affiche une tour à 2 étages de hauteur h chacun et de longueur l pour le premier, L pour le rez-de-chaussée"""
    triangle1=fill_triangle(-(l/2), h, (l/2), h, -(l/2), 0)
    triangle2=fill_triangle(-(l/2), 0, (l/2), h, (l/2), 0)
    triangle3=fill_triangle(-(L/2), 0, (L/2), 0, -(L/2), -h)
    triangle4=fill_triangle(-(L/2), -h, (L/2), -h, (L/2), 0)
    return overlay(triangle1, triangle2, triangle3, triangle4)
show_image(tour(0.5,0.25,1))
show_image(tour(0.25,0.65,1))

