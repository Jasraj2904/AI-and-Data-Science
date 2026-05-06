with open("Updated.txt") as fp:
    data1 = fp.read()
with open("sample.txt") as fp:
    data2 = fp.read()
data1 += "\n"
data2 += "\n"
print("Merging Files ....")
with open("Merged.txt" , "w") as fp:
    fp.write(data1)
    fp.write(data2)