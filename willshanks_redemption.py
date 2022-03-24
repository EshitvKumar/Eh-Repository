n = 68567
l = len(str(n))
a = 10 ** (l)
rem = []
s = '0.' + '0' * (l - 1)
while True:
    r = a % n
    d = a // n
    if r in rem:
        break
    rem.append(r)
    r *= 10
    while r < n:
        r *= 10
        s += '0'
    s += str(d)
    a = r

print(s)
print(len(s) - (2 + (l - 1)))
