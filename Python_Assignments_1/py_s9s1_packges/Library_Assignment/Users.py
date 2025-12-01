
class User:
    def __init__(self, name, user_type):
        self.name = name
        self.user_type = user_type    # student/staff

    def show_user(self):
        print("User: ",self.name , "Type: ", self.user_type)
