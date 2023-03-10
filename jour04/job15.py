"""arrondiPro = round(12.3)
print(arrondiPro)
import math
"""

# - - - - - - - - - - - - - - - - - -

# Déclarations des fonctions

# - - - - - - - - - - - - - - - - - -


"""def pos(nombre) :

   

    Renvoie la valeur de l'exposant en puissance de 10 en écriture scientifique

    n = 120, la fonction renvoie 2

     n = 1,2 la fonction renvoie 1

    n = 0.012, la fonction renvoie -2

    Pour un nombre inférieur à 1, cela correspond à la position après la virgule.



    if nombre > 0 :

        return( int(n))

    elif nombre < 0 :

        return( math.floor( math.log10(-nombre)))

    else :

        return(0)"""
L = [22.4, 4.0,16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
def ajout(liste,x):
    liste += [x]
    return liste
def arrondir():
    liste1 = []
    for n in L:
        if n > float(.5):
            ajout(liste1, int(n))
        else:
             ajout(liste1, int(n-1))
print(arrondir())