def sumOfTwo(a,b,v):
    for x in a:
        for y in b:
            if x+y==v:
                return True
    return False
A=[5,8,5,8,5,8,4,6,5,4]
B=[5,7,2,8,1,10]
V=18
print(sumOfTwo(A, B, V))