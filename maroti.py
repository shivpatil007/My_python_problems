from time import sleep
a = [ 6, 0, 0,0,0,5,1,0,5,38,8,0, 0, 0, 5,0,0,3,5,1, 30, 0, 0, 5, 3, 0]
i = j = 0
while j < len(a):
    if i == j and a[i] != 0:
        i += 1
        j += 1
    elif i == j:
        j += 1
    elif a[j] == 0:
        j += 1
    else:
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
        i+=1
    sleep(2)
    print(a)
    
print(a)
