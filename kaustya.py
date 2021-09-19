n = int(input())
ed = [int(input()) for _ in range(n)]
john = [int(input()) for _ in range(n)]
ed_max = int(input())
jo_max = int(input())
sum = 0

while n:
    x = max(ed)
    y = max(john)
    if x >= y and ed_max:
        ed.pop(ed.index(max(ed)))
        sum += x
        ed_max -= 1
    elif x < y and jo_max:
        john.pop(ed.index(max(john)))
        sum += y
        jo_max -= 1
    n -= 1
print(sum)
