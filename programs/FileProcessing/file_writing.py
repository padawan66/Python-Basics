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


# with open("bear.txt",mode="r") as bear_file:   
#     file_content = bear_file.read()[:90]
#     file_txt = open("first.txt",mode="x") # x mode will create the file if doesn't exust and writes into it
#     file_txt.write(file_content)
#     file_txt.close()

with open("bear.txt",mode="r") as bear_file:   
    file_content = bear_file.read()[:90]
    file_txt = open("first.txt",mode="a") # a mode will append the data to the existing file
    file_txt.write(file_content)
    file_txt.close()

with open("bear.txt",mode="r") as bear_file:   
    file_content = bear_file.read()[:90]
    file_txt = open("first.txt",mode="a+") # a+ mode will allow to read and write data simultaneously
    file_txt.write(file_content)
    file_txt.seek(0) # this will set the cursor to the original position
    content = file_txt.read()
    print(content)
    file_txt.close()