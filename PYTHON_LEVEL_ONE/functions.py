def my_func(param1 = 'default'):
    """

    :param param1:
    """
    print("My f {}".format(param1))


my_func()


#lambda expression

my_list = list(range(8))

def even_bool(num):
    return num%2 == 0

evens = filter(even_bool, my_list)
print(list(evens))


evens2 = filter(lambda num:num%2 == 0, my_list)
print(list(evens2))