i=0
while i<101:
    if i % 5 == 0 and i % 3 == 0:
        print("fizzbuzz")
        i+=1
    elif i % 3 == 0:
        print("fizz")
        i+=1
    elif i % 5 == 0:
        print("buzz")
        i+=1
    print(i)   
    i+=1