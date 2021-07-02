def fibo(n):

    if n == 1 or n == 2:
        result = 1
    bot_up = [0, 1, 1]

    for i in range(2, n):
        bot_up.append(bot_up[1]+bot_up[2])
        bot_up.pop(0)

    return bot_up[2]


n = int(input())
print(fibo(n-1))
