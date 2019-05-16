

def jolyJ(li1):
    fflag = 0
    fres = 0
    rflag = 0
    rres = 0

    n = len(li)

    t2 = 0

    for i in range(0,n-1):

        t = li1[i]
        t3 = li1[i+1]
        #print(t,t3)

        if t > t3:
            t1 = t - t3
        else:
            t1 = t3 - t

        if i == 0:
            t2 = t1
            continue
        else:
            if i == 1:

                if t2 == t1 + 1 and fflag == 0:
                    fflag = 1

                elif t2 == t1 - 1 and rflag == 0:
                    rflag = 1

            if t2 != t1+1 and fflag == 1:
                fres = 1

            elif t2 != t1-1 and rflag == 1:
                rres = 1

            t2 = t1

    if fflag == 1 and fres == 0:
        return  1
    elif rflag == 1 and rres == 0:
        return  1
    else:
        return 0





print("Enter a number ")
n = input()

li = []

for i in range(len(n)):
    #print(n[i])
    li.append(int(n[i]))

res = jolyJ(li)

if res == 1:
    print("YES")
else:
    print("NO")
