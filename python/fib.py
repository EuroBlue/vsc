
def fib(n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        else:
            print(n)
            return (fib(n-1)+fib(n-2))
d=int(input("d="))
print("result is "+str(fib(d)))