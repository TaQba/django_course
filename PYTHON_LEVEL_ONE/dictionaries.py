#dictionaries are hash tables
my_stuff = {'key1': 'cat', 'key2':'dog', 'key3': {'123': [1,1,3,'grabMe']}}
print(my_stuff['key3']['123'][3].upper())


my_stuff = {'lunch': 'pizza', 'bfast':'eggs'}
my_stuff['lunch'] = 'pasta'
my_stuff['dinner'] = 'burger'
print(my_stuff)