#Global Scope

age = 20


#Local scope ( functional scope)

def hello():
    age = 18
    print(f'Hello person, you are {age} years old1')


#hello()
#print(f'This is the global variable {age} years old')

#Enclosing variable scope
#accessiing the closest scope variable within a function

def greeting():
    number = 10

    def quantify():
        print(f'you are number {number} in yhe queue!')

    quantify()
    print('The local variable is:',number)

#reeting()

#Changing a global variable withing a function

def say_your_age():
    global age
    age = 50
    print('The cahnged global variable within a func is:',age)

#say_your_age()


#Changing a local variable within an inner func

def outer_func():
    outer_variable = 5
    def inner_func():
        #altering the local variable
        nonlocal outer_variable
        outer_variable = 6
        print(f'inner func variable is: {outer_variable} ')
    inner_func()
    print('The outer variable is:',outer_variable)

outer_func()