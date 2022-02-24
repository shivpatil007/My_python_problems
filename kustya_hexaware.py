def is_prime(n):
    from math import sqrt

    
    
    prime_flag = 0
      
    if(n > 1):
        for i in range(2, int(sqrt(n)) + 1):
            if (n % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            return 1
        else:
            return 0
    else:
        return 0

arr_prime=[]
arr_non=[]

for _ in range(int(input())):
    x=int(input())
    if is_prime(x):
        arr_prime.append(x)
    else:
        arr_non.append(x)

arr_non.sort()
c=len(arr_prime)
if len(arr_non)>c:
    for _ in range(c+1):
        arr_non.pop()
    print(sum(arr_non))
elif c-1==len(arr_non):
    print(0)
elif c> len(arr_non):
    for _ in range(len(arr_non)+1):
        arr_prime.pop()
    print(sum(arr_prime))
    










