x = int(input())
if x > 0:
    y = 2 * x - 10
elif x == 0:
    y = 0
elif x < 0:
    y = 2 * abs(x)
print('y = ', x)
