

#use this after installing pandas library 
# This takes a csv file as the input which has two columns and gives the mean of each of the column.
# It also prints the mean of one column st1 which can be accessed as seen in the code.
import pandas
import time
import os

while True:
    if os.path.exists("/Users/tejasdongre/Tejas/Personal/Python/10_real_world_app_course/python_apps/python-apps-master/programs/ModulesRelated/temps-today.csv"):
        content = pandas.read_csv("/Users/tejasdongre/Tejas/Personal/Python/10_real_world_app_course/python_apps/python-apps-master/programs/ModulesRelated/temps-today.csv")
        print(content.mean())
        print(content.mean()["st1"])
    else:
        print("file does not exist")
    time.sleep(10)
