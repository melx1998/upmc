import studentlib.gfx
def sablier(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5):
    """float**11*(str)-> Image
    Construit une image représentant 2 triangles pleins sommet à sommet (sablier) reliant les 5 points (x0, y0); (x1,y1), (x2,y2), x(3,y3), (x4,y4), (x5,y5)"""
    triangle1=fill_triangle(x1, y1, x2, y2, x3, y3)
    triangle2=fill_triangle(x3, y3, x4, y4, x5, y5)
    return overlay(triangle1, triangle2)

show_image (sablier(-1, 0.5, 1, 0.5, 0, 0, -1, -0.5, 1, -0.5))
show_image (sablier(-0.5, 0.5, 0.5, 0.5, 0, 0, -0.5, -0.5, 0.5, -0.5))
show_image (sablier(-1, 0.5, 1, 0.5, 0, 0, -1, -0.5, 1, -0.5))
    
