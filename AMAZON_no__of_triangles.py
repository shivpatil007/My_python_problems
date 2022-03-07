#Given an unsorted array of positive integers, find the number of triangles that
#  can be formed with three different array elements as three sides of triangles.
# For a triangle to be possible from 3 values, the sum of any of the two values
# (or sides) must be greater than the third value (or third side).

a = [4, 3, 5, 7, 6]
a.sort()
count = 0
for i in range(len(a) - 1, 0, -1):
    l = 0
    r = i - 1
    while l < r:
        if a[l] + a[r] > a[i]:
            count += r - l
            r -= 1
        else:
            l += 1
print(count)