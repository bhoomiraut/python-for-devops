file = open("demo.txt", "r+") # OPEN & r+ means- first read and then write
print(file.read()) # OPERATION i.e. read content of that file
file.write("Hello Dosto, kya haal chaal")
file.close() # CLOSE

file1 = open("myfile.txt", "w")  
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
print(file1.read())
file1.write("Hello \n")          # write single line
file1.writelines(L)              # write multiple lines
file1.close()              