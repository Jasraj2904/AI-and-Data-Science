def multiple_one_iteration(n,m):
    result = 0
    result = n * m
    return result
def multiple_n_iterations(n,m):
    result = 0
    for i in range(m):
        result = result + n
    return result
n = int(input("Enter a number: "))
m = int(input("Enter the multiplier: "))
ans1 = multiple_one_iteration(n,m)
ans2 = multiple_n_iterations(n,m)
print(f"Result using one iteration: {ans1}")
print(f"Result using n iterations: {ans2}")