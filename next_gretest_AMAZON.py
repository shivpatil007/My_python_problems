a = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
]
import time

print(len(a))
mid = len(a) // 2
x = 1
while x:
    if a[mid] == 0:
        mid = ((mid + 1) + len(a)) // 2
    elif a[mid] == 1:
        if a[mid - 1] == 1:
            mid = mid // 2
        else:
            print(mid)
            x = 0
    print(mid)
    time.sleep(1)