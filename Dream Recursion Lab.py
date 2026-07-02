print("==========Part 1==========")
print("The two rules for recursion are:")
print("1. Base case: The simplest instance of the problem that can be solved directly.")
print("2. Recursive case: The instance of the problem that can be solved by breaking it down into smaller instances of the same problem.")
print()
print("==========Part 2==========")
print("Counting down from 1 to 10 using recursion:")
def count_up(n):
    if n > 10:
        return
    print(n)
    count_up(n + 1)
count_up(1)
print()
print("==========Part 3==========")
print("Countdown showing build and unwind of the recursion stack:")
def countdown(n):
    if n == 0:
        print("Reached the base case!")
        return
    print("Going down:", n)
    countdown(n - 1)
    print("Coming up:", n)
countdown(5)
print()
print("==========Part 4==========")
print("Calculating factorial using recursion:")
def factorial(n):
    if n == 1:
        return 1
    answer = n * factorial(n - 1)
    print(f"factorial({n}) = {answer}")
    return answer
number = 5
print(f"The factorial of {number} is: {factorial(number)}")
print()
print("==========Part 5==========")
print("Stack overflow example:")
def crash():
    print("Calling Again")
    crash()
try:
    crash()
except RecursionError:
    print("Recursion Error Occured")
    print("Reason: There was no base case")
    print("So Python kept creating recursive calls until the stack limit was reached")
    print("This is called a stack overflow error")