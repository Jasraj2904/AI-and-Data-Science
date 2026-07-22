def ways(stairs, path=""):
    if stairs == 0:
        print(path.strip())
        return 1
    if stairs < 0:
        return 0
    one_step = ways(stairs - 1, path + "1 ")
    two_steps = ways(stairs - 2, path + "2 ")
    return one_step + two_steps
def trace_ways(stairs, path="", level=0):
    print("  " * level + f"ways({stairs})")
    if stairs == 0:
        print("  " * level + "Reached base case")
        return
    if stairs < 0:
        print("  " * level + "Invalid path")
        return
    trace_ways(stairs - 1, path + "1 ", level + 1)
    trace_ways(stairs - 2, path + "2 ", level + 1)
def paren(s, l, r, p, n):
    if r == n:
        print("".join(s))
        return 1
    total = 0
    if l < n:
        s[p] = "{"
        total += paren(s, l + 1, r, p + 1, n)
    if r < l:
        s[p] = "}"
        total += paren(s, l, r + 1, p + 1, n)
    return total
def main():
    while True:
        print("\n===== STAIR CLIMB AND BRACE BUILDER =====")
        print("1. Stair Climb")
        print("2. Trace Stair Climb Call Tree")
        print("3. Balanced Brace Builder")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            n = int(input("\nEnter number of stairs: "))
            print("\nPossible paths:")
            total = ways(n)
            print("\nTotal ways:", total)
        elif choice == "2":
            n = int(input("\nEnter number of stairs: "))
            print("\nRecursive Call Tree:")
            trace_ways(n)
        elif choice == "3":
            n = int(input("\nEnter number of brace pairs: "))
            s = [""] * (2 * n)
            print("\nValid balanced brace combinations:")
            total = paren(s, 0, 0, 0, n)
            print("\nTotal combinations:", total)
        elif choice == "4":
            print("\nProgram ended.")
            break
        else:
            print("\nInvalid choice. Please try again.")
main()