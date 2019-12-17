x = 10
y = 'w'
student_grades = [1,23,45]


student_grades = list(range(1,20))  ## this includes one and excludes 20
student_grades = list(range(1,20,2)) # the third argument is the step

# list is mutable ( it has append method)
# dir(list) gives all the functionaities that can be performed by the lst datatype
# help(list.sort)  this gives the details of the attribute/function  present in the list datatype

rainfall = [4.5,5,"test",[1,2,3]]   # The list can contain non homogenous content as well
rainfall = rainfall.__add__(["Damn!!"]) 


rainfall.append("Yeeeha")
#print(rainfall)
average = sum(student_grades) / len(student_grades)
#print("average of the students", average)

monday_temperature = [9.1,8.8,7.5]
monday_temperature.append(4.7)
monday_temperature.extend([4.7])
print("Appended with the list",monday_temperature)


print("index of the  list",monday_temperature.index(9.1))
print("popping of the  list",monday_temperature.pop())
print("Getting an item from an index" , monday_temperature.__getitem__(0), monday_temperature[0])
print("slicing of the list", monday_temperature[1:4], monday_temperature[:4],monday_temperature[2:])

monday_temperature = [9.1,8.8,7.5]
print("Negative index of the list", monday_temperature[-3], monday_temperature[:-2],monday_temperature[-2:])

