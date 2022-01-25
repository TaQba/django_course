s = 'Global Variable !'

def func():
    l = 10

    print(locals())
    print(globals()['s'])

# func()


def hello(name='Jakub'):
    return "Hello " + name


print(hello())

#assign function as variable
mynewgreet= hello
print(mynewgreet())


def hello2(name='Jakub'):
    print( "The Hello() function  has been run !")

    def greet():
        return "This string is insise GREET()"

    def welcome():
        return "This string is insise WELCOME()"

    if name == "Jakub":
        return greet
    else:
        return welcome
x = hello2()
print(x())


#pass function as args
def hello3():
    return 'Hi Jakub'

def other(func):
    print("hello3")
    print(func())

other(hello3)

print('# decorator')
# decorator


def new_decorator(func):

    def wrap_func():
        print("Code before executing FUNC()")
        func()
        print("FUNC() has been called")

    return wrap_func

@new_decorator
def func_needs_decorator():
    print("This function is need of decorator!")


# func_needs_decorator = new_decorator(func_needs_decorator)
func_needs_decorator()




