import os
import time
while True:
    if os.path.exists("/Users/tejasdongre/Tejas/Personal/Python/10_real_world_app_course/python_apps/python-apps-master/programs/FileProcessing/data.txt"):
        with open("/Users/tejasdongre/Tejas/Personal/Python/10_real_world_app_course/python_apps/python-apps-master/programs/FileProcessing/data.txt") as file :
            print(file.read())
    else:
        print("File does not exist")
        print(__file__)
    time.sleep(5)