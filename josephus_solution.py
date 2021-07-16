# josephus function
def josephus(n, k):
    k -= 1
    death = 0
    deathPool = list(range(1, n + 1))
    while len(deathPool) > 1:
        death += k
        death = death % len(deathPool)
        print(deathPool[death])
        deathPool.pop(death)
    print("survivor")
    return deathPool

n = int(input("enter value for n"))
k = int(input("enter value for k"))
print(josephus(n, k))