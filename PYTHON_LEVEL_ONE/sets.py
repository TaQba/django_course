# tuples are immutable sequences
# sets  are unordered collections of unique elements
# booleans are True or False statements

#bool
True
False

# tuples
t = (1,True,'a')
print(t[0])
# t[0] = 2 # error is immutable

# set
x = set()
x.add(1)
x.add(2)
x.add(4)
x.add(4)
x.add(0.4)
print(x)