n=int(input())
for _ in range(n):
  p,q=map(int,input().split(" "))
  
  j=0
  while p!=0 and q!=0:
    if p>=q:
      p=p-q
    else:
      q=q-p
    j+=1
  print(j)