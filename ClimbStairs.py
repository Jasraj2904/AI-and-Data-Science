def ways(stairs, path=[]):
    if stairs == 0:
        print(path)
        return 1
    if stairs < 0:
        return 0
    return ways(stairs - 1, path + [1]) + ways(stairs - 2, path + [2])
stairs = int(input("Enter the number of stairs: "))
total = ways(stairs)
print("Total ways:", total)