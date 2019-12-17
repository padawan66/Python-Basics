arr = [1,2.3]
print("len function",len(arr))  

print("max function ", max(arr))

student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]

filtered = filter(lambda x: x == 10.0,student_grades)

print("filter function which takes lambda",len(list(filtered)))

print("lower function" , "TEST".lower())
