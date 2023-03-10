L = [10,20,30,20,10,50,60,40,80,50,40]
def ajout(liste,x):
    liste += [x]
    return liste
liste1 = []
for n in L:
  if n not in liste1:
    ajout(liste1, n)

print(liste1)