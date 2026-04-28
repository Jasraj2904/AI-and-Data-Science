file_name="sample.txt"
file=open(file_name,'w')
file.write("Apple\nBanana\nCherry\nMango\n")
file.close()
file=open(file_name,'a+')
file.write("Orange\nGrapes\n")
file.close()
file=open(file_name,'r')
count=0
line=file.readline()
while line!="":
    count+=1
    line=file.readline()
file.close()
print("Total number of lines in the file:",count)