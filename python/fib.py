dic = { 0 : 1, 1 : 1,}
# def startFib(n: int) -> int:
#     if n in dic:
#             return(dic[n])
#     else:
#         print(n)
#         x={n:fib(n)}
#         dic.update(x)
#         print(dic)
def fib(n: int) -> int:
        if n in dic:
            return(dic[n])
        else:
            dic.update({n:(fib(n-1)+fib(n-2))})
            return dic[n]
d=int(input("d="))
print("result is "+str(fib(d)))