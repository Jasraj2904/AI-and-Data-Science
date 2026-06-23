print("=" * 50)
print("      BINARY TO DECIMAL CONVERTER")
print("=" * 50)
binary = input("Enter a Binary Number: ")
valid = True
for digit in binary:
    if digit not in ['0', '1']:
        valid = False
        break
if not valid:
    print("\nInvalid Binary Number!")
else:
    decimal = 0
    power = len(binary) - 1
    print("\nConversion Steps:")
    print("-" * 40)
    for digit in binary:
        value = int(digit) * (2 ** power)
        print(f"{digit} × 2^{power} = {value}")
        decimal += value
        power -= 1
    print("-" * 40)
    print("Decimal Number =", decimal)
print("\nThank You!")