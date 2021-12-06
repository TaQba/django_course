d = {'one': 1, 'two': 2 , 'tree':3}

for k in d:
    print(k)
    print(d[k])


my_pairs = [(1,2),(3,4),(5,6)]
for (tup1,tup2) in my_pairs:
    print(tup1)
    print(tup2)


i = 1
while i < 5:
    print("i is {}".format(i))
    i = i+1


#list range
list(range(0,20,2))

for iter in range(10):
    print(iter)


#list comprehention

x = [1,2,3,4,5]
out  = []
for num in x:
    out.append(num**2)

print(out)
out2 = [num**2 for num in x]
print(out2)