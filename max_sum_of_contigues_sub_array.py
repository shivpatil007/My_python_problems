a=[-2,-3,4,-1,-2,5,-46,-31,3,5,35,-36,2,3,-3,-65]

maxx=a[0]
i=0
for k,j in enumerate(a):
    i+=j
    if i<0:
        i=0
    elif maxx<i:
        print(k)
        maxx=i
print("final")
print(maxx)
