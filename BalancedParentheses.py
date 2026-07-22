def paren(s, l, r, p, n):
    if r == n:
        print("".join(s))
        return
    if l < n:
        s[p] = "{"
        paren(s, l + 1, r, p + 1, n)
    if r < l:
        s[p] = "}"
        paren(s, l, r + 1, p + 1, n)
n = int(input("Enter number of pairs: "))
s = [""] * (2 * n)
print("Valid combinations:")
paren(s, 0, 0, 0, n)