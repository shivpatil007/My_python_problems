#Equilibrium index of an array is an index such that the sum of elements at lower
#  indexes is equal to the sum of elements at higher indexes

a = [-7, 1, 5, 2, -4, 3, 0]
summ = sum(a)
left_sum = 0
for i, num in enumerate(a):
    summ -= num
    if summ == left_sum:
        print(i)
        break
    left_sum += num

print(-1)