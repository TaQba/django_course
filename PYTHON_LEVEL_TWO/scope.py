x = 25

def my_func():
    x = 50
    return x

print(x)
print(my_func())


#local
# lambda x: x**2

#Enclosing function locals
name ='this is global name!'

def greet():
    # name = 'sammy'
    def hello():
        print("hello " + name)
    hello()

greet()


# local 2
x = 50
def my_func(x):
    print('x is:', x)
    x = 200
    print('local x is:', x)

my_func(x)
print(x)


#global
x = 50
def my_func():
    global x
    x  = 1000

print('Before function call, x is: ',x)
my_func()
print('After function call, x is: ',x)

