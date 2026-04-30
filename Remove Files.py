file = open("Test.txt", "r")
for line in file:
    if not (line.startswith("Data")):
        print(line)
file.close()
if (line.startswith("Data")):
        print(line)
file.close()
