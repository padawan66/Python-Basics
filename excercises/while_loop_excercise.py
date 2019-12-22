username = "test"
while username!= "test1":
    username = input("Enter username ")
    print("hello %s" %username)
    print(username == "test1")

while True:
    username = input("Enter username")
    if username!= "testusername":
        print(username)
        continue
    else:
        break