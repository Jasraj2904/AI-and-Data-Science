print("========== PART 1 : Peel Digits ==========")
num = int(input("Enter a number: "))
temp = abs(num)
print("\nPeeling digits:")
while temp > 0:
    digit = temp % 10
    print("Digit:", digit)
    temp = temp // 10
    print("Remaining Number:", temp)
print("\n========== PART 2 : Reverse Number (Recursion) ==========")
def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n // 10, rev * 10 + n % 10)
number = int(input("Enter a number to reverse: "))
print("Reversed Number:", reverse_number(abs(number)))
print("\n========== PART 3 : Reverse Word (Recursion) ==========")
def reverse_word(word):
    if len(word) <= 1:
        return word
    return reverse_word(word[1:]) + word[0]
text = input("Enter a name or word: ")
print("Reversed Word:", reverse_word(text))
print("\n========== PART 4 : Power of 4 Checker ==========")
def is_power_of_4(n):
    if n == 1:
        return True
    if n < 1 or n % 4 != 0:
        return False
    return is_power_of_4(n // 4)

numbers = [1, 2, 4, 8, 16, 32, 64, 100, 256, 1024]
print("\nTesting predefined list:")
for num in numbers:
    if is_power_of_4(num):
        print(num, "-> Power of 4")
    else:
        print(num, "-> Not a Power of 4")
student_num = int(input("\nEnter your own number to test: "))
if is_power_of_4(student_num):
    print(student_num, "is a Power of 4")
else:
    print(student_num, "is NOT a Power of 4")
print("\nProgram Completed Successfully!")
