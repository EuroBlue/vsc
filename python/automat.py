o=1
s=0
KS=0
TG=0
MK=0
JK=0
y=0
mog=[1,2,3,4,0]
b=0
k=0
mog2=[0,1,2]

def storn(k,s,KS,TG,MK,JK,x):
    if x==1:
        l=int(input("Wie viele karten wohlen sie lцschen?"))
        while l>KS:
            KS=0
            MN(KS,TG,MK,JK,s)
        else:
            KS = KS - l
            MN(KS,TG,MK,JK,s)
    elif x==2:
        l=int(input("Wie viele karten wohlen sie lцschen?"))
        while l>TG:
            TG=0
            MN(KS,TG,MK,JK,s)
        else:
            TG=TG-l
            MN(KS,TG,MK,JK,s)
    elif x==3:
        l=int(input("Wie viele karten wohlen sie lцschen?"))
        while l>MK:
            MK=0
            MN(KS,TG,MK,JK,s)
        else:
            MK=MK-l
            MN(KS,TG,MK,JK,s)
    elif x==4:
        l=int(input("Wie viele karten wohlen sie lцschen?"))
        while l>JK:
            JK=0
            MN(KS,TG,MK,JK,s)
        else:
            JK=JK-l
            MN(KS,TG,MK,JK,s)
def isint(wv):
  try:
    float(wv)
  except ValueError:
    test=2
  else:
    test=1
  return test

def WK(k,s,KS,TG,MK,JK):
    mog=[1,2,3,4,0]
    while k in mog:
        mog=[1,2,3,4,0]
        if k ==0:
            wlk(k)
            KS=0
            TG=0
            MK=0
            JK=0
            g=0
            k=0
            s=0
            k = int(input("Bitte waehlen sie karte die sie kaufen wollen"))
            WK(k,s,KS,TG,MK,JK)
        elif k==1:
            KS = KS + 1
            s = s + 3
            f=int(input("Wohlen sie noch ein ticket? 1-Ja 2-Nein"))
            TW(f,KS,TG,MK,JK,k,s,b)
        elif k==2:
            TG = TG + 1
            s = s + 10
            f=int(input("Wohlen sie noch ein ticket? 1-Ja 2-Nein"))
            TW(f,KS,TG,MK,JK,k,s,b)
        elif k==3:
            MK = MK + 1
            s = s + 60
            f=int(input("Wohlen sie noch ein ticket? 1-Ja 2-Nein"))
            TW(f,KS,TG,MK,JK,k,s,b)
        elif k==4:
            JK = JK + 1
            s = s + 210
            f=int(input("Wohlen sie noch ein ticket? 1-Ja 2-Nein"))
            TW(f,KS,TG,MK,JK,k,s,b)

def wlk(k):
    print("Willkommen!")
    print("Restart - 0")
    print("Kurzstraeke 3 Euro - 1")
    print("Tageskarte 10 Euro - 2")
    print("Monatskarte 60 Euro - 3")
    print("Jahreskarte 210 Euro - 4")

def wlk2():
    print("Kurzstraeke 3 Euro - 1")
    print("Tageskarte 10 Euro - 2")
    print("Monatskarte 60 Euro - 3")
    print("Jahreskarte 210 Euro - 4")

def FG(schein):
    stueck=[100,50,20,10,5,2,1,0.5,0.2,0.1,0.05,0.02,0.01]
    if schein in stueck:
        stueck=[100,50,20,10,5,2,1,0.5,0.2,0.1,0.05,0.02,0.01]
        test=2
    else:
        print("Fake")
        test=1
    return test

def RG(g,k,s,f,y):
    stueck=[100,50,20,10,5,2,1,0.5,0.2,0.1,0.05,0.02,0.01]
    z=0
    while g is "X" or f==0 or z is "X" or y==3:
        wlk(k)
        KS=0
        TG=0
        MK=0
        JK=0
        g=0
        k=0
        s=0
        k = int(input("Bitte waehlen sie karte die sie kaufen wollen"))
        WK(k,s,KS,TG,MK,JK)
    g=int(g)
    while g<s:
        z = input(str(s-g) + " Euro bite [Abruch - X]")## Bezahlung
        if z is "X":
            wlk(k)
            KS=0
            TG=0
            MK=0
            JK=0
            g=0
            k=0
            s=0
            k = int(input("Bitte waehlen sie karte die sie kaufen wollen"))
            WK(k,s,KS,TG,MK,JK)
        else:
            if FG(int(z))==1 :
                z = input(str(s-g) + " Euro bitte [Abruch - X]")
            else:
                g = g + int(z)

    if g > s :
        r = g - s
        if r in stueck:
            print(r)

        else:
            while r > 100:
                r = r - 100
                print("100")

            while r > 50 and r < 100:
                r = r - 50
                print("50")

            while r >= 20 and r < 100 and r < 50:
                r = r - 20
                print("20")
            while r >= 10 and r < 100 and r < 50 and r < 20:
                r = r - 10
                print("10")
            while r >= 5 and r < 100 and r < 50 and r < 20 and r < 10:
                r = r - 5
                print("5")
            while r >= 2 and r < 100 and r < 50 and r < 20 and r < 10 and r < 5:
                r = r - 2
                print("2")
            while r >= 1 and r < 100 and r < 50 and r < 20 and r < 10 and r < 5 and r < 2:
                r = r - 1
                print("1")
            while r >= 0.5 and r < 100 and r < 50 and r < 20 and r < 10 and r < 5 and r < 2 and r < 1:
                r = r - 0.5
                print("0.5")
            while r >= 0.2 and r < 100 and r < 50 and r < 20 and r < 10 and r < 5 and r < 2 and r < 1 and r < 0.5:
                r = r - 0.2
                print("0.2")
            while r >= 0.1 and r < 100 and r < 50 and r < 20 and r < 10 and r < 5 and r < 2 and r < 1 and r < 0.5 and r < 0.2:
                r = r - 0.1
                print("0.1")
            while r >= 0.05 and r < 100 and r < 50 and r < 20 and r < 10 and r < 5 and r < 2 and r < 1 and r < 0.5 and r < 0.2 and r < 0.1:
               r = r - 0.05
               print("0.05")
            while r >= 0.02 and r < 100 and r < 50 and r < 20 and r < 10 and r < 5 and r < 2 and r < 1 and r < 0.5 and r < 0.2 and r < 0.1 and r < 0.05:
                r = r - 0.02
                print("0.02")
            while r >= 0.01 and r < 100 and r < 50 and r < 20 and r < 10 and r < 5 and r < 2 and r < 1 and r < 0.5 and r < 0.2 and r < 0.1 and r < 0.05 and r < 0.02:
                r = r - 0.01
                print("0.01")
            while r > 0 and r < 100 and r < 50 and r < 20 and r < 10 and r < 5 and r < 2 and r < 1 and r < 0.5 and r < 0.2 and r < 0.1 and r < 0.05 and r < 0.02 and r < 0.01:
                r = r - 0.01
                print("0.01")
                
    while g == s:##Finnish
        print("Danke fuer den Einkauf.")
        exit()
    print("Danke fuer den Einkauf.")
    exit()

def MN(KS,TG,MK,JK,s):
    if KS>0:
        print("KurzstrГ¤ke wurde" + str(KS) + " mal gewГ¤hlt. Das betrГ¤gt fГјr die alleine " + str(KS*3) + " Euro")
    if TG>0:
        print("Tageskarte wurde" + str(TG) + " mal gewГ¤hlt. Das betrГ¤gt fГјr die alleine " + str(TG*10) + " Euro")
    if MK>0:
        print("Monatskarte wurde" + str(MK) + " mal gewГ¤hlt. Das betrГ¤gt fГјr die alleine " + str(MK*60) + " Euro")
    if JK>0:
        print("Jahreskarte wurde" + str(JK) + " mal gewГ¤hlt. Das betrГ¤gt fГјr die alleine " + str(JK*210) + " Euro")
    print("Summe ins gesamt betraegt " + str(KS*3+TG*10+MK*60+JK*210) + " Euro")
    st=int(input("Wollen sie was stornieren? [Ja-1 Nein-2]"))
    while st==1:
        if KS>0 and TG==0 and MK==0 and JK==0:
            if KS==1:
                x=KS
                print("Die einziege Fahrkarte wurde gelГ¶scht Wahlen sie neuen Fahrkarten.")
                x=int(x)-1
                y=3
                RG(b,k,s,f,y)
            else:
                x=KS
                wv=input("Wie viele karten wollen sie stornieren?")
                while isint(wv)==2:
                    print("Das ist keine zahl!")
                    wv=input("Wie viele karten wollen sie stornieren?")
                while int(wv)>x:
                    print("Diese zahl is mehr als anzahl euren karten")
                    wv=input("Wie viele karten wollen sie stornieren?")
                while int(wv)<x:
                    x=int(x)-int(wv)
                    print("Sie haben " + str(wv) + " Fahrkarten storniert.")
                    MN(KS,TG,MK,JK,s)
                while int(wv)==x:
                    print("Sie haben alle Fahrkarten storniert. Wahlen sie neuen Fahrkarten.")
                    RG(b,k,s,f)
        elif KS==0 and TG>0 and MK==0 and JK==0:
            if TG==1:
                x=TG
                print("Die einziege Fahrkarte wurde gelГ¶scht Wahlen sie neuen Fahrkarten.")
                x=int(x)-1
                y=3
                RG(b,k,s,f,y)
            else:
                x=TG
                wv=input("Wie viele karten wollen sie stornieren?")
                while isint(wv)==2:
                    print("Das ist keine zahl!")
                    wv=input("Wie viele karten wollen sie stornieren?")
                while int(wv)>x:
                    print("Diese zahl is mehr als anzahl euren karten")
                    wv=input("Wie viele karten wollen sie stornieren?")
                while int(wv)<x:
                    x=int(x)-int(wv)
                    print("Sie haben " + str(wv) + " Fahrkarten storniert.")
                    MN(KS,TG,MK,JK,s)
                while int(wv)==x:
                    print("Sie haben alle Fahrkarten storniert. Wahlen sie neuen Fahrkarten.")
                    RG(b,k,s,f,y)
                WK(k,s,KS,TG,MK,JK)
        elif KS==0 and TG==0 and MK>0 and JK==0:
            x=MK
            if MK==1:
                MK=x
                print("Die einziege Fahrkarte wurde gelГ¶scht Wahlen sie neuen Fahrkarten.")
                x=int(x)-1
                y=3
                RG(b,k,s,f,y)
            else:
                x=MK
                wv=input("Wie viele karten wollen sie stornieren?")
                while isint(wv)==2:
                    print("Das ist keine zahl!")
                    wv=input("Wie viele karten wollen sie stornieren?")
                while int(wv)>x:
                    print("Diese zahl is mehr als anzahl euren karten")
                    wv=input("Wie viele karten wollen sie stornieren?")
                while int(wv)<x:
                    x=int(x)-int(wv)
                    print("Sie haben " + str(wv) + " Fahrkarten storniert.")
                    MN(KS,TG,MK,JK,s)
                while int(wv)==x:
                    print("Sie haben alle Fahrkarten storniert. Wahlen sie neuen Fahrkarten.")
                    RG(b,k,s,f,y)
                WK(k,s,KS,TG,MK,JK)
        elif KS==0 and TG==0 and MK==0 and JK>0:
            x=JK
            if JK==1:
                MK=x
                print("Die einziege Fahrkarte wurde gelГ¶scht Wahlen sie neuen Fahrkarten.")
                x=int(x)-1
                y=3
                RG(b,k,s,f,y)
            else:
                x=JK
                wv=input("Wie viele karten wollen sie stornieren?")
                while isint(wv)==2:
                    print("Das ist keine zahl!")
                    wv=input("Wie viele karten wollen sie stornieren?")
                while int(wv)>x:
                    print("Diese zahl is mehr als anzahl euren karten")
                    wv=input("Wie viele karten wollen sie stornieren?")
                while int(wv)<x:
                    x=int(x)-int(wv)
                    print("Sie haben " + str(wv) + " Fahrkarten storniert.")
                    MN(KS,TG,MK,JK,s)
                while int(wv)==x:
                    print("Sie haben alle Fahrkarten storniert. Wahlen sie neuen Fahrkarten.")
                    RG(b,k,s,f,y)
                WK(k,s,KS,TG,MK,JK)
            WK(k,s,KS,TG,MK,JK)
        else:
            mog3=[1,2,3,4]
            if KS>0:
                print("KurzstrГ¤ke - 1")
            if TG>0:
                print("Tageskarte - 2")
            if MK>0:
                print("Monatskarte - 3")
            if JK>0:
                print("Jahreskarte - 4")
            alpha=int(input("WГ¤hlen sie welche Fahrkarte sie zu erst stornieren wolt"))
            while alpha not in mog3:
                alpha=int(input("WГ¤hlen sie welche Fahrkarte sie zu erst stornieren wolt"))
            else:
                storn(k,s,KS,TG,MK,JK,alpha)
    else:
        y=1
        s=KS*3+TG*10+MK*60+JK*210
        RG(b,k,s,f,y)

def TW(f,KS,TG,MK,JK,k,s,b):
    mog2=[0,1,2]
    mog=[1,2,3,4,0]
    while f not in mog2:
        mog2=[0,1,2]
        f=int(input("Wohlen sie noch ein ticket? 1-Ja 2-Nein"))        
    if f==1:
        k = int(input("Bitte waehlen sie karte die sie kaufen wollen"))
        WK(k,s,KS,TG,MK,JK)
        while k not in mog:
            mog=[1,2,3,4,0]
            print("Es solchen Fahrschein gibs nicht")
            k = int(input("Bitte waehlen sie karte die sie kaufen wollen"))            
    elif f==2:
        MN(KS,TG,MK,JK,s)
        b=input(str(KS*3+TG*10+MK*60+JK*210) + " Euro bitte [Abruch - X]")
        RG(b,k,s,f)
    elif f==0:
        KS=KS-KS
        TG=TG-TG
        MK=MK-MK
        JK=JK-JK
        s=s-s
        RG(b,k,s,f)
######################################################
print("Willkommen!")
print("Restart - 0")
print("Kurzstraeke 3 Euro - 1")
print("Tageskarte 10 Euro - 2")
print("Monatskarte 60 Euro - 3")
print("Jahreskarte 210 Euro - 4")


k = int(input("Bitte waehlen sie karte die sie kaufen wollen"))

while k not in mog:
    mog=[1,2,3,4,0]
    print("Es solchen Fahrschein gibs nicht")
    k = int(input("Bitte waehlen sie karte die sie kaufen wollen"))

while k in mog:
    mog=[1,2,3,4,0]
    if k ==0:
        wlk(k)
        KS=KS-KS
        TG=TG-TG
        MK=MK-MK
        JK=JK-JK
        s=s-s
        k = int(input("Bitte waehlen sie karte die sie kaufen wollen"))
    elif k==1:
        KS = KS + 1
        s = s + 3
        f=int(input("Wohlen sie noch ein ticket? 1-Ja 2-Nein"))
        TW(f,KS,TG,MK,JK,k,s,b)
    elif k==2:
        TG = TG + 1
        s = s + 10
        f=int(input("Wohlen sie noch ein ticket? 1-Ja 2-Nein"))
        TW(f,KS,TG,MK,JK,k,s,b)
    elif k==3:
        MK = MK + 1
        s = s + 60
        f=int(input("Wohlen sie noch ein ticket? 1-Ja 2-Nein"))
        TW(f,KS,TG,MK,JK,k,s,b)
    elif k==4:
        JK = JK + 1
        s = s + 210
        f=int(input("Wohlen sie noch ein ticket? 1-Ja 2-Nein"))
        TW(f,KS,TG,MK,JK,k,s,b)