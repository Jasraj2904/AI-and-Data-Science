def linear_recursion(n):
    if n == 0:
        print("Reached the base case")
        return
    print(n)
    linear_recursion(n - 1)
print("\n ================= Linear Recursion ================= \n")
linear_recursion(5)
def tail_recursion(n):
    if n == 0:
        return
    print(n)
    tail_recursion(n - 1)
print("\n ================= Tail Recursion ================= \n")
tail_recursion(5)
def head_recursion(n):
    if n == 0:
        return
    head_recursion(n - 1)
    print(n)
print("\n ================= Head Recursion ================= \n")
head_recursion(5)
def increasing_decreasing(n):
    if n == 0:
        return
    print(n)
    increasing_decreasing(n - 1)
    print(n)
print("\n ================= Increasing Decreasing Recursion ================= \n")
increasing_decreasing(5)
def tree_recursion(n):
    if n == 0:
        return
    print(n)
    tree_recursion(n - 1)
    tree_recursion(n - 1)
print("\n ================= Tree Recursion ================= \n")
tree_recursion(3)