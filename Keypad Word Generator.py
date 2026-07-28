keypad = {
    "2": ["A", "B", "C"],
    "3": ["D", "E", "F"],
    "4": ["G", "H", "I"],
    "5": ["J", "K", "L"],
    "6": ["M", "N", "O"],
    "7": ["P", "Q", "R", "S"],
    "8": ["T", "U", "V"],
    "9": ["W", "X", "Y", "Z"]
}
def combinations(digits, current):
    if len(digits) == 0:
        print(current)
        return
    digit = digits[0]
    if digit not in keypad:
        combinations(digits[1:], current)
        return
    for letter in keypad[digit]:
        combinations(digits[1:], current + letter)
digits = input("Enter digits (2-9): ")
combinations(digits, "")