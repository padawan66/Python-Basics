
my_file = open("fruits.txt")  # the contents of the file is printed only once even though two print statements are 
#available because the cursor would have reached the end of the file and so it prints only an empty string
#print(my_file.read())
#print(my_file.read())

# inorder to print the contents as many times as possible we need to store the contents of the file in a temporary variable
# and print the variable
content = my_file.read()
#print(content)
#print(content)

# if you close the file , then you can read the file again.
my_file.close()
my_file = open("fruits.txt")
print(my_file.read())

my_file.close()
my_file = open("fruits.txt")
print(my_file.read())


# reading the first 90 charecters of the file
text_file = open("bear.txt")
content = text_file.read()
text_file.close()
index = 0
text = ""
for letter in content:
    if index < 90:
        if text == "":
            text = letter
            index = index+1
        else :
            text+= letter
            index = index+1
            
print(text)

# optimized way to read first 90 charecters
file = open("bear.txt")
content = file.read()
file.close()
print(content[:90])


# this function gives the occurences of a character in a file
def get_occurances(character,filepath):
    opened_file = open(filepath)
    content = opened_file.read()
    opened_file.close()
    return content.count(character)

print(get_occurances("f","bear.txt"))

# using with keyword which kind of acts as a kotlin with
with open("bear.txt") as my_file:
    content = my_file.read()
print(content)