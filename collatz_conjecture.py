n = float(input())
l = []

while n not in l:
    l.append(n)
    if n % 2 == 0:
        n = n / 2
    else:
        n = 3 * n + 1

# print(l)
if n == l[0]:
    print(n)
else:
    print(l[-1])