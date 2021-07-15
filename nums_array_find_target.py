from time import time
x=time()
nums=[3,6,5,3,5,32,4,45,51,651,65,5,84,265,484,65,5,8,49,616,58,484,8,6,16,4,14,64,4,4,541,63,414,1,68,4,64,84,58]
target=21
a={}
for i,j in enumerate(nums):
    if j in a:
        print(a[j],i)
        break
    else:
        a[target-j]=i
print("Done")
print(time()-x)