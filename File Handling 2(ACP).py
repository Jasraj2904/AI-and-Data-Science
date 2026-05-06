import os
file1 = "file1.txt"
file2 = "file2.txt"
merged_file = "merged.txt"
if not os.path.exists(file1):
    with open(file1, "w") as f:
        f.write("Apple\nBanana\nMango\n")
if not os.path.exists(file2):
    with open(file2, "w") as f:
        f.write("Banana\nOrange\nApple\n")
with open(file1, "r") as f1:
    data1 = f1.readlines()
with open(file2, "r") as f2:
    data2 = f2.readlines()
merged_data = data1 + data2
unique_lines = []
for line in merged_data:
    if line not in unique_lines:
        unique_lines.append(line)
with open(merged_file, "w") as f:
    f.writelines(unique_lines)
print("Merged File Content (without duplicates):")
with open(merged_file, "r") as f:
    print(f.read())