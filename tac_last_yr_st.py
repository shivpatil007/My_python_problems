a = int(input())
t = int(input())
marks = []
time = []
for i in range(a):
    marks.append(int(input()))
    time.append(int(input()))


def subset_sum(numbers, target, partial=[]):
    s = sum(partial)
    if s == target:
        print(partial)
    if s >= target:
        return

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1:]
        subset_sum(remaining, target, partial + [n])


subset_sum(time, 10)
