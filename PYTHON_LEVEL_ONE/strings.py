#STRINGS
my_string = 'abcdefg'
print(my_string[0])
print(my_string[-1])

#Slices

print(my_string[4:])
print(my_string[:3])
print(my_string[1:3])
print(my_string[::2])
print(my_string.upper())
print(my_string.capitalize())

my_string = "Hello World"
print(my_string.split('l'))

# print Formatting
x = "Item one: {x} Item Two: {y}".format(x="dog", y='cat')
print(x)