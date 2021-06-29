



t=int(input())
for i in range(t):
    small=0
    large=0
    l=int(input())
    r=int(input())
    if(l==r):
        print(0)
        continue
    x=r
    for j in range(l,r+1):
        flag = False

       

        for k in range(2, j):
            if (j % k) == 0:
                print("LLLLLLLLLL")
                print(j)
                flag = True
                # break out of loop
                break
        if flag==False and j>1:
            small=j
                
            print( small)
            break    
                    
                
        
    while(x>l):
        flag = False

        # prime numbers are greater than 1
        if x > 1:
            # check for factors
            for k in range(2, j):
                if (x % k) == 0:
                    # if factor is found, set flag to True
                    flag = True
                    # break out of loop
                    break
                if flag==True:
                    x-=1
                    continue
                else:
                    large=x
                    
                    print(large)
                    break
        x-=1
    print(large-small)
