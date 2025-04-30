import os # Import the "operating system" module os.

# os.chdir("/Users/guido/Documents")
# text files
file = open("hist.txt")
f_read = file.read()
print(file)
print(f_read)
print("file stream position",file.tell())
print(len(f_read))
file.close()
#print(" printing the directory")
#print(dir(file))


# text files
myfile = open("hist.txt","r")
print(myfile.read(5))
#to get the file stream current position
print("file stream position",myfile.tell())
myfile.close()

print()

# buffered binary files
myfile = open("hist.txt","rb")
print()
print(myfile.read(150))
print("file stream position",myfile.tell())
myfile.close()


# raw files
myfile = open("hist.txt","rb", buffering = 0)
print()
print(myfile.read(150))
myfile.close()

# readline and readlines()-list returned
myfile = open("hist.txt","r")
print()
print(myfile.readline())
print(myfile.readlines())
myfile.close()






















# reading a file using 
file = open("hist.txt", "r")
count = 0
for line in file:
    count = count + 1
    print(count, ": ", line, sep="", end="")

for count, line in enumerate(open("hist.txt", "r")):
    print(count + 1, ": ", line, sep="", end="")






















#list comprehension to open a file
lines = [line.strip() for line in open('hist.txt')]
print("list comprehension",lines)
print()

# processing of file
myfile = open("hist.txt","r")
text_string = myfile.read()
word_list = text_string.split()
print("the words are:",word_list)

new_text = text_string.replace("python","c++")
print("the new text:",new_text)

#myfile.write(new_text)
myfile.close()


print(os.getcwd())
myfile = open("hist.txt","r")
print(myfile.read())
print(myfile.seek(5))
print(myfile.tell())
print()










    

os.getcwd()




























