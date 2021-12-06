#####################################
#### PART 9: FUNCTION EXERCISES #####
#####################################


# Complete the tasks below by writing functions! Keep in mind, these can be
# really tough, its all about breaking the problem down into smaller, logical
# steps. If you get stuck, don't feel bad about having to peek to the solutions!

#####################
## -- PROBLEM 1 -- ##
#####################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:

# arrayCheck([1, 1, 2, 3, 1])
# arrayCheck([1, 1, 2, 4, 1])
# arrayCheck([1, 1, 2, 1, 2, 3])


def arrayCheck(nums):
    seq = (1,2,3)
    out = False
    i = 0
    while i < len(nums)-2:
        if seq[0] == nums[i] and seq[1] == nums[i+1] and seq[2] == nums[i+2]:
            out = True

        i = i+1

    return out

print(arrayCheck([1, 1, 2, 3, 1]))
print(arrayCheck([1, 1, 2, 4, 1]))
print(arrayCheck([1, 1, 2, 1, 2, 3]))

#####################
## -- PROBLEM 2 -- ##
#####################

# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:

# stringBits('Hello') => 'Hlo'
# stringBits('Hi') => 'H'
# stringBits('Heeololeo') => 'Hello'

def stringBits(str):
    out = ''
    i = 1
    for l in str:
        if i%2 != 0:
            out = out + l
        i += 1
    print(out)

stringBits('Hello')
stringBits('Hi')
stringBits('Heeololeo')

#####################
## -- PROBLEM 3 -- ##
#####################

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#
# end_other('Hiabc', 'abc')  => True
# end_other('AbC', 'HiaBc')  => True
# end_other('abc', 'abXabc')  => True


def end_other(a, b):
    a = a.lower()
    b = b.lower()

    return a[-(len(b)):] == b or b[-(len(a)):] == a

print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))
print(end_other('ab2', 'abXabc'))

#####################
## -- PROBLEM 4 -- ##
#####################

# Given a string, return a string where for every char in the original,
# there are two chars.

# doubleChar('The')  => 'TThhee'
# doubleChar('AAbb')  => 'AAAAbbbb'
# doubleChar('Hi-There')  => 'HHii--TThheerree'

def doubleChar(str):
    out = ''
    for l in str:
        out += l + l
    return out

print(doubleChar('The'))
print(doubleChar('AAbb'))
print(doubleChar('Hi-There'))



#####################
## -- PROBLEM 5 -- ##
#####################

# Read this problem statement carefully!

# Given 3 int values, a b c, return their sum. However, if any of the values is a
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!
#
# Examples:
#
# no_teen_sum(1, 2, 3)  => 6
# no_teen_sum(2, 13, 1)  => 3
# no_teen_sum(2, 1, 14)  => 3

#def no_teen_sum(a, b, c):
  # CODE GOES HERE
#def fix_teen(n):
  # CODE GOES HERE

#####################
## -- PROBLEM 6 -- ##
#####################

# Return the number of even integers in the given array.
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4])  => 3
# count_evens([2, 2, 0])  => 3
# count_evens([1, 3, 5])  => 0

def count_evens(nums):
    out = 0
    for i in nums:
        if i%2 == 0:
            out += 1
    return out

print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([2, 2, 0]))
print(count_evens([1, 3, 5]))
