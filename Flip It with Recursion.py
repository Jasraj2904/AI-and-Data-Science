print("\n========== PART 1 : Extract Digits ==========")
num = int(input("Enter a number: "))
temp = abs(num)
print("\nDigits extracted from right to left:")
if temp == 0:
    print(0)
while temp > 0:
    digit = temp % 10
    print("Digit:", digit)
    temp //= 10
print("\n========== PART 2 : Reverse Number ==========")
number = int(input("Enter a number to reverse: "))
def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n // 10, rev * 10 + n % 10)
print("Reversed Number:", reverse_number(abs(number)))
print("\n========== PART 3 : Reverse String ==========")
text = input("Enter a word or name: ")
def reverse_string(s):
    if s == "":
        return ""
    return reverse_string(s[1:]) + s[0]
print("Reversed String:", reverse_string(text))
print("\n========== PART 4 : Power of 4 ==========")
def is_power_of_4(n):
    if n == 1:
        return True
    if n <= 0 or n % 4 != 0:
        return False
    return is_power_of_4(n // 4)
numbers = [1, 2, 4, 8, 16, 20, 64, 100, 256]
print("\nChecking sample numbers:")
for i in numbers:
    if is_power_of_4(i):
        print(i, "is a Power of 4")
    else:
        print(i, "is NOT a Power of 4")
user_num = int(input("\nEnter your own number to test: "))
if is_power_of_4(user_num):
    print(user_num, "is a Power of 4")
else:
    print(user_num, "is NOT a Power of 4")
print("\n========== Program Completed ==========")