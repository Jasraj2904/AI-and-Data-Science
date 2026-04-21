file_name = input("Enter the file name: ")

file = open(file_name, 'r')
lines = file.readlines()

print("Total number of lines:", len(lines))

file.close()