a = int(input("a"))
b = int(input("b"))
c = int(input("c"))
def longueur(a , b ,c):
    return longueur(a , b , c)
    
if a <= b+c and b <= a+c and c <= a+b:
        print("triangle")
        if a == b and b == c:
            print("triangle equilaterale")
        elif a == b or a == c:
            print("triangle isocele")
        elif a*a + b*b == c*c or b*b + c*c == a*a or c*c + a*a == b*b :
            print("triangle rectangle")
else:
    print("PAS TRIANGLE")

