# try:
#     name = input('Enter your name:')
#     year_born = input('Year you were born:')
#     age = 2026 - year_born
#     print(f'You are {name}. And your age is {age}.')
# except:
#     print('Something went wrong')


# try:
#     name = input('Enter your name:')
#     year_born = input('Year you were born:')
#     age = 2019 - year_born
#     print(f'You are {name}. And your age is {age}.')
# except TypeError:
#     print('Type error occured')
# except ValueError:
#     print('Value error occured')
# except ZeroDivisionError:
#     print('zero division error occured')

# try:
#     name = int(input('Enter your name: '))
#     year_born = input('Year you born:')
#     age = 2026 - int(year_born)
#     print(f'You are {name}. And your age is {age}.')
# except TypeError:
#     print('Type error occur')
# except ValueError:
#     print('Value error occur')
# except ZeroDivisionError:
#     print('zero division error occur')
# else:
#     print('I usually run with the try block')
# finally:
#     print('I alway run.')
# try:
#     name = input('Enter your name:')
#     year_born = input('Year you born:')
#     age = 2026 - year_born
#     print(f'You are {name}. And your age is {age}.')
# except Exception as e:
#     print(e)


# #  UNPACKING LIST, TUPPLE AND SET
# def sum_of_five_nums(a, b, c, d, e):
#     return a + b + c + d + e

# lst = [1, 2, 3, 4, 5]
# print(sum_of_five_nums(*lst))

# # UNPACKING DICTIONARY
# diction = {"Name".lower(): "Abubakr", "Country".lower(): "Nigeria", "Age".lower(): 25}
# def infor(name, country, age):
#     return f"{name} is my name, I'm from {country} and my age is {age}"

# print(infor(**diction))

# # PACKING LISTS OR DICTIONARIES

# def packed_list(*lists):
#     print(lists)
#     report = ""
#     for word in lists:
#         report += word + " "

#     return report

# print(packed_list("How", "are", "you", "doing", "today"))


# # PACKING DICTIONARIES

# def packing_person_info(**kwargs):
#     # check the type of kwargs and it is a dict type
#     # print(type(kwargs))
#     # Printing dictionary items
#     for key in kwargs:
#         print(f"{key} = {kwargs[key]}")
#     return kwargs

# print(packing_person_info(name="Olugbade",
#       country="Nigeria", city="Abuja", age=25))


# # SPREADING 

# lst_one = [1, 2, 3]
# lst_two = [4, 5, 6, 7]
# lst = [0, *lst_one, *lst_two]
# print(lst)         
# country_lst_one = ['Nigeria', 'Ghana', 'Nairobi']
# country_lst_two = ['Spain', 'Canada', 'Paris']
# nordic_countries = [*country_lst_one, *country_lst_two]
# print(nordic_countries) 


# # ZIP

# fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
# vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
# fruits_and_veges = []
# for f, v in zip(fruits, vegetables):
#     fruits_and_veges.append({'fruit':f, 'veg':v})

# print(fruits_and_veges)
