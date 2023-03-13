def draw_rect(C,L):
    for i in range(1,L+1):
        for j in range(1,C+1):
            if i == 1 and j!=1 and j!=C  or i == L and j!=C and j !=1:  
                print("-", end=" ")
            elif j == 1 or j == C :
                print("|", end=" ")
            else:
                print(" ",end=" ")
        print()
draw_rect(10, 3)