def greet_user():
    user = input("Input user  ")
    print(f"Hello user {user}")

#greet_user()
def greet_user_old(user):
    message = "Hi %s"  % user
    return message.title()

print(greet_user_old("test"))