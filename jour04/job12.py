liste = [45,5,47,32,22,78] 
"""def longueur(liste):
    compteur = 0
    for i in liste:
        compteur += 1
    return compteur
def ajout(liste,x):
    liste += [x]
    return liste"""
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
liste_triee = tri_insertion(liste)
print(liste_triee)

    


