# # 3.3
# def check_all_types(listed_items):
#     items_types = []
#     for i in range(0,len(listed_items)):
#         if type(listed_items[i]) == type(listed_items[i-1]):
#             items_types.append(True)
#         else:
#             items_types.append(False)
#     if items_types.__contains__(False):
#         return False
#     else:
#         return True

# print(check_all_types([1,2,3,7,5,6,7,2.5]))

# # 3.4
# import keyword

# def is_valid_variable(data):
#     data = str(data)
#     report = False
#     if keyword.iskeyword(data):
#         report = False
#     else:
#         if data[0] == '_' or data[0].isalpha():
#             for i in range(len(data)):
#                 if data[i].isdigit() or data[i].isalpha()  or data[i] == '_':
#                     report = True

#                 else:
#                     report = False
#         else:
#             report = False
#     return report
# print(is_valid_variable('hhd@'))

# #3.5.1
# from countries_data import countries


# def most_spoken_languages(countries):
#     languages = []
#     for country in countries:
#         for key, value in country.items():
#             if key == 'languages':
#                 languages += value
#     languages = sorted(languages)
#     language_count = {}
#     for lang in languages:
#         if lang in language_count:
#             language_count[lang] += 1
#         else:
#             language_count[lang] = 1
#     counts = []
#     for val in language_count.values():
#         counts.append(val)
#     sort_counts = sorted(counts)

#     last_10 = sort_counts[int(len(sort_counts))-10:]

#     last_10 = set(last_10)
    
#     last_10 = list(last_10)
#     last_10 = sorted(last_10)

#     result = ''

#     for i in range(len(last_10)-1,-1, -1):
#         for lc_key, lc_value in language_count.items():
#             if last_10[i] == lc_value:

#                 result += f'{lc_key} is one of the 12 most spoken languages in the world with {lc_value} countries\n'
    
#     return result
# print(most_spoken_languages(countries))


# # 3.5.2
# from countries_data import countries
# def most_populated_countries(countries):
#     population = []
#     result = ''
#     country_names = []
#     for country in countries:
#         for tag in country:
#             if tag == 'population':
#                 val = country.__getitem__(tag)

#                 population.append(val)
#             if tag == 'name':
#                 val = country.__getitem__(tag)
#                 country_names.append(val)
            
   
#     dict_country_popul = dict(zip(country_names, population))


#     population = set(population)
#     report = ''
#     sort_population = sorted(population)
#     last_ten = sort_population[len(sort_population)-10:]
#     last_ten = sorted(last_ten)

#     for i in range(len(last_ten)-1,-1, -1):
#         for key, value in dict_country_popul.items():
#             if  last_ten[i] == value:

#                 report += f'{key} is one of the 10 most populated countries in the world with a total of {value} citizens\n'
    
#     return report


# print(most_populated_countries(countries))


