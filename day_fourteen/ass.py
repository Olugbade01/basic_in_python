## Exercise Level 1

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

# # 2.7
# def E_country(country):
#     if str(country).startswith('M' or 'm'):
#         return True
#     else:
#         return False

# E_countries = filter(E_country, countries)

# # print(list(E_countries))

# # 2.8
# def to_upper(country):
#     return country.upper()


# result = filter(E_country, map(to_upper, countries))

# print(list(result))

# # 2.9
# def is_string(item):
#     if str(item).isidentifier():
#         return True
#     else:
#         return False


# def get_string_list(list_items):
#     string_items = filter(is_string, list_items)
#     return list(string_items)

# print(get_string_list(['Hello', '1hdjkd', 'dress', '_gdhjdj', 'hdgk;hdjhd']))

# # 2.10
from functools import reduce

# def sum_all_numb(m, n):
#     return m+n

# sum_numbs = reduce(sum_all_numb, numbers)
# print(sum_numbs)

# # 2.11

# def conc_list(text1, text2):
#     return text1 + ", " + text2

# def func_reduce(listed_items):
#     conc_contries = listed_items[0:len(listed_items)-1]

#     concatenated = reduce(conc_list, conc_contries).__add__(' and ').__add__(listed_items[len(listed_items)-1]).__add__(' are north European countries')
    

#     return concatenated


# print(func_reduce(countries))


# 2.12


# from ../../../30-Days-Of-Python import data

# import sys 
# import os

# countries_path = os.path.abspath('/mnt/c/Users/HP/30-Days-Of-Python/data')

# sys.path.append(countries_path)

# import countries
# countries_list = countries.countries
# def land_countries(country):
#     country = str(country)
#     if country.__contains__('Land') or country.__contains__('land'):
#         return True
#     else:
#         return False

# def island_countries(country):
#     country = str(country)
#     if country.__contains__('island') or country.__contains__('Island'):
#         return True
#     else:
#         return False

# def stan_countries(country):
#     country = str(country)
#     if country.__contains__('stan') or country.__contains__('Stand'):
#         return True

#     else:
#         return False

# def ia_countries(country):
#     country = str(country)
#     if country.__contains__('ia') or country.__contains__('Ia'):
#         return True

#     else:
#         return False

    
# def categorize_countries(countries_list):
 
#     land_country = filter(land_countries, countries_list)
    
#     island_country = filter(island_countries, countries_list)

#     ia_country = filter(ia_countries, countries_list)

#     stan_country = filter(stan_countries, countries_list)
    
#     result = {
#         'Land': list(land_country),
#         'Island': list(island_country),
#         'Ia': list(ia_country),
#         'Stan': list(stan_country)

#     }
#     return result

# print(categorize_countries(countries_list))

# # 2.13
# import string
# def first_letter(letter):
    
#     letter = str(letter).upper()
#     def countries_with_letter(country):

#         if str(country).startswith(letter):
#             return True

#         else:
#             return False
#     return countries_with_letter

    

# def country_first_letter_count(countries_list):
#     result = {

#     }
#     for alpha in string.ascii_uppercase:
#         operator = first_letter(alpha)
#         result[alpha] = list(filter(operator, countries_list))
#         result[alpha] = len(result[alpha])


#     return result
# print(country_first_letter_count(countries_list))

# # 2.14
# def get_first_ten_countries(listed_countries):

#     return listed_countries[0:10]

# print(get_first_ten_countries(countries_list))
# # 2.15    
# def get_last_ten_countries(countries_list):
#     return countries_list[len(countries_list)-10:]


# print(get_last_ten_countries(countries_list))


# Excercise Level 3
import json

import os 

file_dir = os.path.dirname(os.path.abspath('/mnt/c/Users/HP/30-Days-Of-Python/data'))
file_path = os.path.join(file_dir, 'data', 'countries_data.json')

with open(file_path, 'r') as file:
    file_content = json.load(file)



# 3.1

# # 3.1.1

# print(file_content)

# # 3.1.2
# def capital_getter(file):
#     return file['capital']
# print(sorted(file_content, key = capital_getter))

# # OR

# print(sorted(file_content, key = lambda capitals: capitals['capital']))

# # 3.1.3
# print(sorted(file_content, key=lambda population: population['population']))

# # OR

# def population_getter(dict_list):
#     return dict_list['population']

# print(sorted(file_content, key=population_getter))

# 3.2


# # 3.3
# sorted_popul = sorted(file_content, key= population_getter)
# print(sorted_popul[len(file_content)- 10:])