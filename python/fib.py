dic = { 0 : 1, 1 : 1,}
def fib(n: int) -> int:
        if n in dic:
            return(dic[n])
        else:
            dic.update({n:(fib(n-1)+fib(n-2))})
            return dic[n]
d=int(input("d="))
print("result is "+str(fib(d)))