s = "geekforgeekandgeeksandquizfor"
print(len(s))
a = {}
queue = []
x = []
for i in s:
    if not queue:
        queue.append(i)
        x.append(i)
        print(i, end=" ")
        a[i] = 1
    elif i != queue[0] and a[queue[0]] == 1:
        x.append(queue[0])
        print(queue[0], end=" ")
        if i in a:
            a[i] += 1
        else:
            a[i] = 1
            queue.append(i)
    elif i == queue[0]:
        a[i] += 1
        queue.pop(0)
        while a[queue[0]] != 1:
            queue.pop(0)
        x.append(queue[0])
        print(queue[0], end=" ")

print(len(x))