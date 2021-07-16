def combination(a, b):
    fac_a = 1
    fac_b = 1
    fac_aminb = 1
    for i in range(1, a + 1):
        fac_a *= i
    for j in range(1, b + 1):
        fac_b *= j
    for k in range(1, (a - b) + 1):
        fac_aminb *= k
    return int(fac_a / (fac_b * fac_aminb))

lim = int(input("enter limit"))
for i in range(lim + 1):
    for j in range(i + 1):
        print(combination(i, j), end = ' ')
    print()