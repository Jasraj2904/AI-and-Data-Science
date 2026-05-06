file = open("text.txt" , "w")
file.write("Hello World")
file.close()
with open("text.txt" , "r") as file:
    data = file.readlines()
    print(data)
    for line in data:
        word = line.split()
        print(word)
file.close()