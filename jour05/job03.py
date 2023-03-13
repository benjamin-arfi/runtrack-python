def tapis(n):
    bord = "+"
    for i in range(n+1): 
        bord += "-"
    bord += "+" 
    print(bord)
    for i in range(n+1):
        tapisse = ""
        for j in range (n-i): 
            tapisse +="#"
        tapisse +=" "
        for j in range(i):
            tapisse += "#"
        print("|" + tapisse + "|")
    print(bord)
tapis(10)