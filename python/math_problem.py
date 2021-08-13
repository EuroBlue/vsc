import random as r
yes=0
no=0
def problem(deal):
    global yes
    global no
    arr=[1,2,3]
    a=arr[r.randint(0,2)]
    b=arr[r.randint(0,2)]
    if deal:
        for x in range(0,2):
            if arr[x]!=a and arr[x]!=b:
                arr.pop(x)
                break
        if arr.index(b)==1:
            b=arr[0]
        else:
            b=arr[1]
    if a==b:
        yes=yes+1
    else:
        no=no+1
def main():
    global yes
    global no
    for x in range(100):
        problem(False)
    print(f"YES = {yes}\nNO= {no}")
    yes=0
    no=0
    for x in range(100):
        problem(True)
    print(f"YES = {yes}\nNO= {no}")
if __name__=="__main__":
    main()