# Classes

class User:
    # constructor func
    def __init__(self, name, email):
        self.name = name
        self.email = email





def main():

    user_one = User("Rui", "ruially@mail.com")
    print(user_one.name ,user_one.email,)
    return


if __name__ == "__main__":
    main()