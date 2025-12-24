
# list: order, index, 
# set: no order, no index, unique
# tuple: order, index, constant
# dict: order, index=key, key=value


# crud: create, read, update, delete

# # --- create ---
# di = {'name': 'ali'}
# di.update({'age': 32})
# di['gender'] = 'm'


# # --- read ---
# print(di['name'])
# print(di.get('age'))
# print(di.keys())
# print(di.values())


# # --- update ---
# di['name'] = 'reza'
# di.update({'name': 'reza'})

# # --- delete ---
# print(di.pop('name'))
# # di.popitem()  # random


# iterable
# ----------------------

# # list, set, tuple loop
# li = ('ali', 'reza', 'sara')

# for name in li:
#     print(name.upper())




# loop for dict
# ------------------
# di = {
#     'name': 'ali',
#     'age': 32,
#     'gender': 'male',
#     'email': 'ali@g.com'
# }

# for k in di.keys():
#     print(k)

# for v in di.values():
#     print(v)

# for k, v in di.items():
#     print(k, v)


# create a list from another list
# li = [1, 2, 3, 4, 5]
# li2 = []

# for num in li:
#     li2.append(num ** 2)
    
# print(li2)




# li = ['ali', 'reza', 'ali', 'reza', 'ali', 'sara', 'ali', 'sara', 'ali', 'ali']
# count = li.count('ali')
# for i in range(count):
#     li.remove('ali')
    
# print(li)

# while True:
#     count = li.count('ali')
#     if count < 1:
#         break
#     li.remove('ali')



users = [
    {'name': 'ali', 'age': 28, 'city': 'tehran', 'children': True},
    {'name': 'reza', 'age': 20, 'city': 'tehran', 'children': True},
    {'name': 'sara', 'age': 38, 'city': 'rasht', 'children': False},
    {'name': 'nima', 'age': 25, 'city': 'karaj', 'children': False},
    {'name': 'ghazal', 'age': 21, 'city': 'rasht', 'children': False},
]

for user in users:
    print(user.get('name'))