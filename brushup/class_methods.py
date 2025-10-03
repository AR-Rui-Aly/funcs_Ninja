class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def post_status(self, status):
        print(f"{self.name} posted status {status}")



user_one = User("Abdul", "abdul@mail.com")
print(user_one.post_status(" I am rui, and i am an engineer!!"))