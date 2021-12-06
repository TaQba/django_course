#list
my_list = [1,2,3]
my_list = ['dsa',2,3.21, True, [1,2,3]]
print(my_list)
print(len(my_list))
print(my_list[0])
print(my_list[-1])


#adding
my_list = ['a', 'b', 'c']
print('Before:')
print(my_list)
my_list[0] = 'jakub'
my_list.append('JT')
print('After')
print(my_list)

list_two = ['x','y','z']
print('Extend')
my_list.extend(list_two)
print(my_list)


#remove
print('Pop')
item = my_list.pop()
print(item)
print(my_list)


#remove
print('Revers')
my_list.reverse()
print(my_list)


matrix = [[1,2,3],[4,5,6],[7,8,9]]
#LIST COMPREHENTION
first_col = [row[0] for row in matrix]
print(first_col)
print(matrix[0][0])

