a = input()

i = 0
j = 0
k = 1
while(i < len(a)):

    if len(a) > i+2 and int(a[i])+int(a[i+1]) == int(a[i+2]):

        i += 1

    elif len(a) > i+3 and int(a[i])+int(a[i+1]) == int(a[i+2] + a[i+3]):

        i += 1

    else:

        break


if i == len(a)-2 or i == len(a)-3:
    print(True)
else:
    print(False)
