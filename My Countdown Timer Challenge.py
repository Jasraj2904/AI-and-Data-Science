import time
def countdown(n):
    if n == 0:
        print("Blast off!")
        return
    print(n)
    time.sleep(1)  
    countdown(n - 1)
def count_up(n):
    if n == 0:
        return
    count_up(n - 1)
    print(n)
def build_unwind(n):
    if n == 0:
        print("Reached the base case!")
        return
    print("Building Stack:" , n)
    build_unwind(n - 1)
    print("Unwinding Stack:", n)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
def stack_overflow():
    print("Calling Again")
    stack_overflow()
while True:
    print("Countdown Timer Challenge")
    print("1. Countdown")
    print("2. Count Up")
    print("3. Build and Unwind Stack")
    print("4. Factorial")
    print("5. Stack Overflow Example")
    print("6. Exit")
    choice = int(input("Enter your choice (1-6): "))
    if choice == 1:
        n = int(input("Enter the starting number for countdown: "))
        countdown(n)
    elif choice == 2:
        n = int(input("Enter the number to count up to: "))
        count_up(n)
    elif choice == 3:
        n = int(input("Enter the number to build and unwind stack: "))
        build_unwind(n)
    elif choice == 4:
        n = int(input("Enter the number to calculate factorial: "))
        result = factorial(n)
        print(f"The factorial of {n} is: {result}")
    elif choice == 5:
        try:
            stack_overflow()
        except RecursionError:
            print("Recursion Error Occurred: Stack overflow due to no base case.")
    elif choice == 6:
        print("Thank you for using the Countdown Timer Challenge!")
        break
    else:
        print("Invalid choice. Please try again.")