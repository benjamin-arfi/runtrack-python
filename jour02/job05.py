def calcul(num1,operator,num2):
    if operator == '+':
        return num1 + num2
    elif operator =="-":
        return num1-num2
    elif operator=="*":
        return num1 * num2
    elif operator== "/":
        return num1/num2  
num1= int(input("num1"))
operator=input("operator")
num2=int(input("num2"))
print(calcul(num1, operator, num2))
