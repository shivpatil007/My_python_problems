a=[5,6,8,2,8,9,3,3,6,4,9,2,10,2,7,3,4,6]

i=a.index(max(a))
total=0
flag1=0
flag2=0
forward=i
backward=i
back1=i
back2=i
while(flag1==0 or flag2==0):
    if len(a)>forward+1:
        forward=a.index(max(a[forward+1:]),forward+1)
        total+=(forward-back1)*a[forward]
        back1=forward
        print("its j-> "+str(forward))
    else:
        flag1=1
    if backward!=0:
        backward=a.index(max(a[:backward]),0,backward)
        total+=(back2-backward)*a[backward]
        back2=backward
        print("its k => "+str(backward))
    else:
        flag2=1

print(total)