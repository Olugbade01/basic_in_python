# def multiply(numb):
#     nul = numb * 7
#     def sum_num():
#         return 7 + nul
#     return sum_num



# result = multiply(10)


# print(result())
# #  Decorator
# def upper_decorator(function):
#     def wrapper():
#         func = function()
#         to_upper = func.upper()
#         return to_upper
#     return wrapper

# def lower_decorator(function):
#     def to_lower():
#         func = function().lower()
#         return func
#     return to_lower


# @lower_decorator
# @upper_decorator
# def perform_action():
#     return "Hello boss"

# print(perform_action())

#  

# def add_10(number):

#     def adder():
#         num = number()
#         return num.__add__(10)
#     return adder

# @add_10
# def number():
#     return 7


# print(number())


# # map()
# # To use map(): map_func = map(function(could be built in), iterable) or map_func = map(lambda x : ....., iterable)


# cube_function = lambda x : x ** 3 

# list_number = [2, 4, 6, 8, 10, 12, 1, 3, 5, 7, 9, 11]

# cube_list = list(map(cube_function, list_number))
# print(cube_list)

# def upper_function(parameter):
#     return parameter.upper()


# name = 'mutiat'
# tuple_names = ('sugar', "wasiu", 'victor ', 'mutiat')

# res = map(upper_function, name)
# result = ''.join(list(res))
# print(result)


# # Filter: filter_func = filter(function(could be an inbuilt), iterable) returns the boolean from the function 

# def is_odd(number):
#     if number % 2 != 0 :
#         return True
#     else:
#         return False


# numbers = [2,3,4,5,6,7,8,9,10, 15, 33]


# list_odd = list(filter(is_odd, numbers))


# print(list_odd)



