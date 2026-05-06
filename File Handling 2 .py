new_file = open("new_file.txt" , "x")
new_file.close()
import os 
print("Checking if file exists or not....") 
if os.path.exists("new_file.txt"): 
    os.remove("new_file.txt")
else:
    print("The file does not exist")
my_file = open("new_file.txt" , "w")
my_file.write("Hello I am Jasraj Singh and I am 15 years old.")
my_file.close()
os.remove("text.txt")
os.rmdir("text.txt")
