from bisect import insort
a=[1,2,3,56,5,46,3,4,9,1,6,3,2,5,323,4,6,3,4,8,9,3,5,7,32,4,6,9,63,685,6,+5,6,5,6,85,6,5]
b=4
c=[]

for i in a:
    if i  not in c:
        insort(c,i,)
print(c)
print(c[len(c)-b])