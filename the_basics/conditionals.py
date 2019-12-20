def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values())/len(value)
    else:
        the_mean = sum(value)/len(value)

    return the_mean


student_grades = {"Student1":4.5 , "Student2":5.5 , "Student5": 6.7}

print("Mean of grades" ,mean(student_grades))