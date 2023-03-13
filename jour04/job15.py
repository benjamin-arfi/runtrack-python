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
liste = [22.4, 4.0,16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
def ajout(liste,x):
    liste += [x]
    return liste
def tri_insertion(liste):
    L = list(liste) # copie de la liste
    N = len(L)
    for n in range(1,N):
        cle = L[n]
        j = n-1
        while j>=0 and L[j] > cle:
            L[j+1] = L[j] # decalage
            j = j-1
        L[j+1] = cle
    return L
def arrondir():
    for n in tri_insertion(liste):
        if n < float((n)+1/2):
            print (int(n))
        else:
            print( int(n+1))
arrondir()