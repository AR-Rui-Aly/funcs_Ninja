# Static methods are not tied to the instances created by the classes or tied to the objects the class will be used on

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    # Here is where you turn a func into a static method by using a decorator to explicitly detach it from the self argument
    @staticmethod
    def validate_email(email):
        return "@" in email and len(email)> 3



# There are two steps to class inheritance
# The first is to pass in the parent class to the child class as an argument
# The second step is to invoke the super() method and chain in the constructor func from the parent class like in the example bellow

class MasterUser(User):
    def __init__(self, name, email,title):
        super().__init__(name, email)
        self.title = title




def main():

    print(User.validate_email('rui@mail.com'))
    super_user_one = MasterUser("Rui", "rui@aly.com", "Engineer")
    print(super_user_one.title)
    return


if __name__ == "__main__":
    main()