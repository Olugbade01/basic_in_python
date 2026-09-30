# Exercise Level 1

# 1.1
# map(), filter() and reduce() has the same format. They all take a function and iterable as arguments, but map and filter returns a list while reduce returns a value
# One distinct difference between the is that reduce is a function from a module called functools while map and filter is a built in function on it own 
# 1.2

# A HOF is a function with function as a parameter or return a function, Closure is a function with an inner function accessing the outer function's variable and returning the inner function while decorator takes a whole function to another function with a wrapper function as the inner and returns the wrapper function.
# # 1.3 
# def factorial(number):
#     facto = 1 
#     for i in range(number+1):
#         if i > 0:
#             facto *= i
#         else:
#             continue
#     return facto

# def square(x):
#     return x**2

# number = [1,2,3,4,5,6,7,8,9,10]

# # square_numbers = map(square, number)
# # print(square_numbers)
# num_factorial = map(factorial, number)
# print(list(num_factorial))

# def is_odd( number ):
#     if number % 2== 0:
#         return False
#     else:
#         return True


# is_odd_numb = filter(is_odd, number)


# print(list(is_odd_numb))

# # 1.4

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for country in countries:
#     print(country)

# # 1.5

# for name in names:
#     print(name)

# # 1.6
# for number in numbers:
#     print(number)

# Excercise Level 2

# # 2.1
# def to_upper(word):
#     word = str(word).upper()
#     return word

# upper_list = map(to_upper, countries)
# print(list(upper_list))

# # 2.2
# def square(numb):
#     return numb ** 2

# square_numbs = map(square, numbers)
# print(list(square_numbs))

# # 2.3
# def to_upper(word):
#     return word.upper()

# name_upper = map(to_upper, names)
# print(list(name_upper))

# # 2.4
# def contains_land(country):
#     if country.__contains__('land'):
#         return True
#     else:
#         return False

# land_country = filter(contains_land, countries)
# print(list(land_country))

# # 2.5

# def country_lenght_6(country):
#     if len(country) == 6:
#         return True
#     else:
#         return False

# length_6 = filter(country_lenght_6, countries)
# print(list(length_6))