import matplotlib.pyplot as plt
while True:
    x=float(input("What to test: "))
    main=x
    y=0
    res=[]
    while x!=1 and x!=-1:
        if x not in res:
            if x%2==1:
                res.append(x)
                x=(x*3)+1
            else:
                res.append(x)
                x=x/2
            y=y+1
            print(x)
        else:
            res.append(x)
            print("Found infinite loop beetween " +str(res[0])+" and "+str(res[y-1]))
            break
    res.append(x)
    print("it comes after " +str(y)+" units")
    x=[]
    for o in range(0,y+1):
        x.append(o)
    plt.plot(x, res)
    plt.xlabel('Index')
    plt.ylabel('outcome')
    plt.title('3x+1 for '+str(int(main)))
    plt.show()