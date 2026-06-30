n = int(input("Find primes up to: "))
primes = [True] * (n + 1)
if n >= 0:
    primes[0] = False
if n >= 1:
    primes[1] = False
p = 2
while p * p <= n:
    if primes[p]:
        for i in range(p * p, n + 1, p):
            primes[i] = False
    p += 1
print("Prime numbers up to", n, "are:")
for i in range(2, n + 1):
    if primes[i]:
        print(i, end=" ")