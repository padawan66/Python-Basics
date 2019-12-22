## for loop over the list

colors = [11, 34, 98, 43, 45, 54, 54]

for color in colors:
    if color>50 :
        print(color)

for color in colors:
    if isinstance(color,int):
        print(color)



for color in colors:
    if isinstance(color,int) and color>50:
        print(color)


## for loop over the dict

student_grades = {"student 1":4.5, "student 2":6.7 , "student 3":7.8}

for grade in student_grades.keys():
    
    print(grade)

for grade in student_grades.items():
    
    print(grade)

for grade in student_grades.values():
    
    print(grade)
 
for key,value  in student_grades.items():
    
    print("Key and value in a string".format(key, value))

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for item in phone_numbers.items():
    print(item[0], ": ", item[1])

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for num in phone_numbers.values():
    print(num.replace("+","00"))

