# Static methods are not tied to the instances created by the classes or tied to the objects the class will be used on

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    # Here is where you turn a func into a static method by using a decorator to explicitly detach it from the self argument
    @staticmethod
    def validate_email(email):
        return "@" in email and len(email)> 3







def main():

    print(User.validate_email('rui@mail.com'))
    return


if __name__ == "__main__":
    main()