# They are used to generate extra logic to a function and to wrapp that func with this logic


# THis is the func that will generate additional logic and wrap the other func
#seacrh for use cases in real life

def decorate_run_marathon_func(wrapped_func):

    def wrapper():
        print("praparing to run the marathon")
        wrapped_func()
        print("finished race")

    return wrapper

@decorate_run_marathon_func
def run_marathon():
    print("Running Marathon")


run_marathon()