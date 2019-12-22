with open("vegetables.txt",mode="w") as my_file:
    my_file.write("Onions")
    my_file.write("Garlic")
    my_file.close()

# opening the file and reading first 90 characters and writing it to another file

with open("bear.txt",mode="r") as bear_file:
    file_content = bear_file.read()[:90]
    file_txt = open("first.txt",mode="w") 
    file_txt.write(file_content)
    file_txt.close()