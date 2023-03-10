
alpha = "abcdefghijklmnopqrstuvwxyz"*10
n=1
i=0

while i+n <= len(alpha):
    print(alpha[i:i+n])
    i += n
    n +=1
