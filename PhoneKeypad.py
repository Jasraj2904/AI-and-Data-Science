keypad = { 
    "2" : ["A" , "B" , "C"],
    "3" : ["D" , "E" , "F"],
    "4" : ["G" , "H" , "I"],
    "5" : ["J" , "K" , "L"],
    "6" : ["M" , "N" , "O"],
    "7" : ["P" , "Q" , "R" , "S"],
    "8" : ["T" , "U" , "V"],
    "9" : ["W" , "X" , "Y" , "Z"]
}
def combinations(digits , current):
    if len(digits) == 0:
        print(current)
        return
    first_digit = digits[0]
    remaining = digits[1:]
    for letter in keypad[first_digit]:
        combinations(remaining , current + letter)
number = input("Enter digits")
print("All Combinations")
combinations(number , "")
count = 1
for digit in number:
    count = count*len(keypad[digit])
print("Total Combinations" , count)