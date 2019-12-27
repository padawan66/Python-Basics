import datetime
print("Printing the date time")
x = datetime.datetime.now()
print("The day and time is ", str(x))
print(x)

# dir(list) gives all the functionaities that can be performed by the lst datatype
# help(list.sort)  this gives the details of the attribute/function  present in the list datatype
# dir(__builtins__) this gives the list of all builtin functions/datatypes - for example - print() and list


import sys
print(sys.prefix) # sys.prefix goves the folder where the python is installed
# in terminal open the folder using the commend 
# open "/filepath"
# In the lib  / python version folder you can see a lot of python modules which are available to import