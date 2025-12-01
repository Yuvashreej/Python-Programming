username = input("Enter your username")
username_length = len(username)
print("Length of the username is: ", username_length)

if username_length<8:
    print("username is too short, please try again")
elif username_length>12:
    print("username is too large, please try again")
else:
    print("username is accceptable")

