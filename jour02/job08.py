def alliment (type,saison):
    if type == fruit and saison == hiver:
        print("“orange, mandarine et kiwi”")
    elif type== fruit and saison== ete:
        print("poire<fraise cassis")
    elif type == legume and saison==hiver:
        print("carotte, topinambour, endive")
    elif type== legume and saison== ete:
        print("artichaut, aubergine,navet")
    return alliment(type, saison)
type = input("type")
saison = input("saison")
fruit = input("fruit")
legume = input ("legume")
hiver = input("hiver")
ete = input ("ete")
print(alliment(type, saison))

    