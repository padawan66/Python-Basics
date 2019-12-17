monday_temp = [9.1,8.8,7.5]
student_grades = {"student1":9.1,"strudent2":8.8,"student3":7.5}
sum_of_vals = sum(student_grades.values())  # .values() function call on the dictionary gives the values present in the dictionary
                                            # .keys() function call on the dictionary gives the keys present in the dictionary
average = sum_of_vals/student_grades.__len__()
print("Average",average)