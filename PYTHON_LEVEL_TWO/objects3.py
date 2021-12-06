# INHERITANCE

class Animal():

    def __init__(self):
        print("Animal Created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):

    def __init__(self):
        #Animal.__init__(self)
        print("Dog Created")

    def bark(self):
        print("Woof")

    def eat(self):
        print("Dog Eating")

# myd = Dog()
# myd.whoAmI()
# myd.eat()
# myd.bark()


# special Methods

class Book():

    def __init__(self, title, author, pages):

        self.title = title
        self.author = author
        self.pages = pages


    def __str__(self):
        return "Title: {}, Author: {}, Pages {}". format(self.title, self.author, self.pages)


    def __len__(self):
         return self.pages

    def __del__(self):
        print('destroy')

b = Book("Python", "JT", 200)
print(len(b))
del(b)