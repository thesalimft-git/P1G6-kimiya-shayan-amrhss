
# se = {1 , 2, 3}
# tu = (1, 2, 3, 'ali', 3)
# di = {'name': 'ali', 'age': 32}


# li = [1, 5, 2, 10, 3, 'a']
# print(li)
# li.append(2)
# li.extend([2, 3, 4])
# li.clear()
# li.count('ali')
# x = li.index(5)
# print(x)
# li.insert(3, 'reza')
# li.pop(6)
# li.remove('ali')
# li.reverse()
# li.sort()
# print(li)



# tu = (10, 20, 'ali', 30, 'reza')
# tu.count('ali')
# tu.index('ali')


# set: no order, no index, no occurrence
s1 = {1, 2, 3}
s2 = {3, 4, 5}

# print(s1.union(s2))
# print(s1.update(s2))

# print(s1.difference(s2))
# print(s1.difference_update(s2))

# print(s1.symmetric_difference(s2))
# print(s1.symmetric_difference_update(s2))


# print(s1.intersection(s2))
# print(s1.intersection_update(s2))


# print(s1.add(4))
# print(s1)


# s1.remove()
# s1.discard()

# print(s1.isdisjoint(s2))

# s1.issubset(s2)
# s1.issuperset(s2)




# shalow copy, deep copy
# x = {'name': 'ali'}
# y = x           # shallow copy
# y = x.copy()    # deep copy

# # print(id(x))
# # print(id(y))

# y['age'] = 32

# print(y)
# print(x)

di = {
    'name': 'ali',
    'age': 32
}

# print(di['name'])
# print(di.get('age'))

# di['new'] = 'new value'
# di['name'] = 'reza'
# # di.update({'new 2': 'new value'})
# print(di)





li = ['ali', 'reza', 'sara']
print(li[0])

di = {
    '0': 'ali',
    '1': 'reza',
    '2': 'sara',
}
print(di['0'])