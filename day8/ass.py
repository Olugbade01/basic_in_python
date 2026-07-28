emptdict = {}
print(type(emptdict))
dog = {
    'name': 'bush',
    'color': 'Green',
    'breed': 'German-Shepard',
    'legs': 4,
    'age': 6
}
student = {
    'first_name': 'Tade',
    'last_name': 'Gbenga',
    'gender':   'Female', 
    'age': 16, 
    'marital status': 'single',
    'skills':   'Dance',
    'country': 'Nigeria', 
    'city': 'Lagos', 
    'address':  'Lekki' 
    
}
# len_student = len(student)
# print(len_student)
# skill_value = student.values()
# print(type(skill_value))
# keys_value = list(skill_value)
# keys_value.append('Football')
# print(keys_value)
# keys = student.keys()
# keys = list(keys)
item = student.items()
print(type(item))
del student['age']
print(student)
del dog
# print(keys)