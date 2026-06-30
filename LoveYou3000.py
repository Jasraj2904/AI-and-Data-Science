start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
if end < 2:
    print("No prime numbers in this range.")
else:
    limit = end
    primes = [True] * (limit + 1)
    primes[0] = False
    if limit >= 1:
        primes[1] = False
    p = 2
    while p * p <= limit:
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1
    print("Prime numbers in the range", start, "to", end, "are:")
    for i in range(max(2, start), end + 1):
        if primes[i]:
            print(i, end=" ")
    print("\n")
    print("Palindrome prime numbers in the range", start, "to", end, "are:")
    for i in range(max(2, start), end + 1):
        if primes[i]:
            original = i
            reverse = 0
            while original > 0:
                digit = original % 10
                reverse = reverse * 10 + digit
                original //= 10
            if i == reverse:
                print(i, end=" ")