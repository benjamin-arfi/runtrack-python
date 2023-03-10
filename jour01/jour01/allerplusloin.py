#coding:utf8
i = 0
caractere = "e"
drapeau = False
# taper requetes
print("ce programme détermine si une chaîne contient ou non le caractère « e »")
chaine = input ("tapez la chaine de caracteres svp : ")

#calcul nombre caractere et conversion en numero
nombre_caractere = len(chaine)

#recherche de la lettre E
while i < nombre_caractere:
	print(i, end = " ")
	if chaine[i] == caractere:
		drapeau = True
		print(chaine[i])
	i = i+1
#affichage
print("l'expression", end =" ")
if drapeau == True:
	print("contient la lettre E")
else:
	print("ne contient pas la lettre E")