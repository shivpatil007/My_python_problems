from itertools import permutations
count=0
n=int(input())
a=[n-1,1,0]


while a[0]-1 not in a:

    a[0]-=1
    if a[1]<a[2]:
        a[1]+=1
    else:
        a[2]+=1
    d=set(permutations(a))
    count+=len(d)
    print(d)
    
    
print(count)