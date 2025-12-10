# # variable, function, loop, condition


# # sum of all number lower than x


# def is_prime(x):
#     it_is_prime = True
#     for i in range(2, x//2):
#         if x % i == 0:
#             it_is_prime = False
#             break
#     return it_is_prime


# def echo_primes(x):
#     for num in range(1, x):
#         if is_prime(num):
#             print(num)


# echo_primes(10)









# positional, keyword argument

# def sum(*args):
#     total = 0
#     for item in args:
#         total += item
    
#     print(total)

# sum()
# sum(1, 1)
# sum(1, 1, 1)
# sum(1, 1, 1, 1)


# print(list(range(10)))
# print(list(range(5, 20)))
# print(list(range(5, 20, 2)))

# def my_range(end, start = 0, step = 1):
#     i = start
#     while i < end:
#         print(i)
#         i += step


# my_range(10)
# my_range(2,10)
# my_range(2, 10, 3)




def my_range(*args):
    start = 0
    step = 1
    if len(args) == 3:
        start = args[0]
        end = args[1]
        step= args[2]
    if len(args) == 2:
        start = args[0]
        end = args[1]
    if len(args) == 1:
        end = args[0]
    
    i = start
    while i < end:
        print(i)
        i += step

my_range(10)
my_range(5, 10)
my_range(10, 100, 5)