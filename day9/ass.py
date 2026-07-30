# # Exercise Level 1: 

# age = int(input('How old are you: '))
# if age > 18: 
#     print('You are old enough to drive')
# else:
#     remain = 18 - age
#     print(f'You need %d more years to learn how to drive'%(remain))

# # Excercise Level 1

# my_age = 20
# your_age = int(input('Enter your age: '))
# dif = abs(my_age - your_age)
# if my_age > your_age:
#     print(f'I\'m %d older than you are, Accord some respect next time')


# # Excercise Level 1 question 3

# a = int(input('Enter a number here: '))
# b = int(input('Enter a second number: '))

# if a > b: 
#     print('a is greater than b')
# elif a < b: 
#     print('a is smaller than b')
# else:
#     print('a is equal to b')

# # Excercise 2: level 2
# # 2.1

# score = int(input('Enter your score here: '))

# if 90 <= score <= 100:
#     print('Your grade is A')
# elif 80 <= score < 90:
#     print('Your grade is B')
# elif 70 <= score < 80:
#     print('Your grade is C')
# elif 60 <= score < 70:
#     print('Your grade D')
# else: 
#     print('Your grade is F')

# # 2.2
# month = input('Enter the month you are! ')
# if month == 'September' or month == 'October' or month == 'December':
#     print('Its Autummn season out there')
# elif month == 'December' or month == 'January' or month == 'February':
#     print('Its Winter season out there!')
# elif month == 'March' or month == 'April' or month == 'May':
#     print('Its the Spring season out there!')
# elif month == 'June' or month == 'July' or month == 'Auguest':
#     print('Its Summer season out there!')
# else: 
#     print('Enter a valid month')

# # 2.3 
 
# fruits = ['banana', 'orange', 'mango', 'lemon']
# text = input('Enter a fruit to check in the list: ')
# if fruits.__contains__(text):
#    print('That fruit already exist in the list')
# else:
#    print(f'The fruit ( %s ) is not there!'%(text))


# # Excercise 3 Level 3 
# # 3.1 
# person={
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_married': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }

# }

# li_item = (person['skills'])
# if person.__contains__('skills'):
#     print(li_item[int(len(li_item)//2)])
#     if li_item.__contains__('Python'):
#         print('Python')
#     if li_item.__contains__('JavaScript') and li_item.__contains__('React') and len(li_item) == 2:
#         print('He is a front end developer')
#     if 'Node' in li_item and li_item.__contains__('Python') and li_item.__contains__('MongoDB'):
#         print('He is a backend developer')
#     if 'React' in li_item and 'Node' in li_item and 'MongoDB' in li_item:
#         print('He is a fullstack developer')
#     else:
#         print('unknown title')