def miror(seq): 
    inv = "" 
    for char in seq: 
        inv = char + inv 
    return inv 

seq = input("rentre ton mot:")
print(miror(seq))