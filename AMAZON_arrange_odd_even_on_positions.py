a = [3, 6, 12, 1, 5, 8]
odd_value_at_queue = []
even_value_at_queue = []
print(a)
for i, j in enumerate(a):
    if i % 2 == 0 and j % 2 != 0:
        if even_value_at_queue:
            x = even_value_at_queue.pop(0)
            a[i], a[x] = a[x], a[i]
        else:
            odd_value_at_queue.append(i)
    elif i % 2 != 0 and j % 2 == 0:
        if odd_value_at_queue:
            x = odd_value_at_queue.pop(0)
            a[i], a[x] = a[x], a[i]
        else:
            even_value_at_queue.append(i)

print(a)
