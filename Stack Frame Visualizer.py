print("="*60)
print("Stack Frame Visualizer")
print("="*60)
#=================================
#Part 1 Linear Recursion
#=================================
def linear_recursion(n):
    print("Entering Frame" ,n )
    if n == 0:
        print("Reached the base case")
        return
    linear_recursion(n - 1)
    print("Returning from Frame" ,n )
print("\n ================= Linear Recursion ================= \n")
linear_recursion(5)
#=================================
#Part 2 Tail Recursion
#=================================
def tail_recursion(n):
    if n == 0:
        print("Reached the base case")
        return
    print("Processing" , n )
    tail_recursion(n - 1)
print("\n ================= Tail Recursion ================= \n")
tail_recursion(5)
#=================================
#Part 3 Head Recursion
#=================================
def head_recursion(n):
    if n == 0:
        print("Reached the base case")
        return
    head_recursion(n - 1)
    print("Processing" , n )
print("\n ================= Head Recursion ================= \n")
head_recursion(5)
#=================================
#Part 4 Increasing Decreasing Recursion
#=================================
def increasing_decreasing(n):
    if n == 0:
        return
    print("Going Down the stack" , n)
    increasing_decreasing(n - 1)
    print("Going Up the stack" , n)
print("\n ================= Increasing Decreasing Recursion ================= \n")
increasing_decreasing(5)
#=================================
#Part 5 Tree Recursion
#=================================
def tree_recursion(n):
    if n == 0:
        print("Reached the base case")
        return
    print("Frame" , n)
    tree_recursion(n - 1)
    tree_recursion(n - 1)
print("\n ================= Tree Recursion ================= \n")
tree_recursion(3)
#=================================
# END OF PROJECT
#================================
print("\n" + "="*60)
print("All Recursion Patterns have been visualized successfully!")
print("="*60)
print("\nThank you for using the Stack Frame Visualizer!")
print("\n END OF PROJECT \n")
