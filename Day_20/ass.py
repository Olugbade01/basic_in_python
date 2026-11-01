# # Excercise Level 1
# # # 1.1
# import urllib.request
import requests
import re
import os
import json
# # option 1 

# site_url = 'https://www.gutenberg.org/cache/epub/5933/pg5933-images.html'
# with urllib.request.urlopen(site_url) as file:
#     raed_ = file.read()
# # print(raed_)
# # Option 2
# response = requests.get(site_url)

# response = response.text

# text_only = re.findall(r'\w+', response)

# word_count = {

# }

# for word in text_only:
#     word = str(word).capitalize()
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
# values = []
# for val in word_count.values():
#     values.append(val)

# sorted_val = sorted(values)
# last_10 = sorted_val[len(sorted_val)-10:]
# report = []
# for i in range(len(last_10)-1, -1, -1):
#     for key, value in word_count.items():
#         if value == last_10[i]:
#             report.append((key, value))
# print(report)


# 2.1
def float_validator(numb):
    
    try:
        float(numb)
        return True
    except:
        return False
def convet_to_float(list_numbs):
    number_float = []
    for numb in list_numbs:
        if float_validator(numb):
            numb = float(numb)
            number_float.append(numb)
        else:
            continue
    return number_float

def average_calculator(listed_nums):
    sums = 0
    for i in range(len(listed_nums)):
        sums += listed_nums[i]
    return round((sums/2), 2)

        

# url_api = 'https://api.thecatapi.com/v1/breeds'

# # the_api_key = live_99PsER2UvaAz0YPhs6CbZ1ZxkSMaF7fUbFiNE8ArP5ijKZoFqvTV7WRR6qhiFcjj

# api_key = os.environ.get("CAT_API_KEY")



# headers = {"x-api-key": api_key}

# api_response = requests.get(url_api, headers=headers)



# result = api_response.json()

# numbs = []
# for each_bread in result:

#     numbs.append(each_bread['weight']['metric'].split('-'))
# list_floated_numbs = []       
# for num in numbs:
#     if len(num) == 2:
#         converted = convet_to_float(num)
#     else:
#         continue

#     list_floated_numbs.append(converted)
   
# # print(list_floated_numbs)
# averages = []
# for floated_number in list_floated_numbs:
#     averages.append(average_calculator(floated_number))

# print(averages)
# # 2.1.1
# print(min(averages))
# # 2.1.2
# print(max(averages))


# # 2.1.3

def median_of_averages(list_averages):
    list_numbers = sorted(list_averages)
    mid_point = len(list_averages)//2
    if len(list_numbers)%2 != 0:
        median = list_numbers[mid_point]
    else:
        median = (list_numbers[mid_point-1]+ list_numbers[mid_point])/2
    return median
# print(median_of_averages(averages))

# # 2.1.4
def find_mean(listed_element):
    sum_numbs = sum(listed_element)
    mean = sum_numbs/len(listed_element)
    return round(mean, 4)
def standard_deviation(elements):
    mean = find_mean(elements)
    bracketed = []
    for x in elements:
        bracketed.append(round(x - mean, 4))
    squared_list = []
    for xi in bracketed:
        squared_list.append(round(xi **2, 4))
    sum_squrs = sum(squared_list)
    stand_devi = (sum_squrs/(len(elements))) ** 0.5
    return round(stand_devi,2)
# print(standard_deviation(averages))

# # 2.2

# life_span = []

# for items in result:
#     life_span.append(items['life_span'].split('-'))
# float_spans = []
# for str_nums in life_span:
#     floated_span = convet_to_float(str_nums)
#     float_spans.append(floated_span)

# xi = []

# for x in float_spans:
#     xi.append(average_calculator(x))

# # 2.2.1
# print(min(xi))

# # 2.2.2
# print(max(xi))

# # 2.2.3
# print(find_mean(xi))
# # 2.2.4
# print(median_of_averages(xi))

# # 2.2.5

# print(standard_deviation(xi))

# # 2.3
# country_breed = {}

# for bread in result:
#     country_name = bread['origin'] 
#     name = bread['name']
#     breads = []
#     if country_name in country_breed:
#         country_breed[country_name] += [name]

#     else:
 
#         country_breed[country_name] = [name]
# table = f'Country Name \t Breeds \t Breed Names \n'
# for key, value in country_breed.items():
#     table += f'{key} \t {len(value)} \t {", ".join(value)} \n'

# print(table)


# 3

response = requests.get(
  'https://api.restcountries.com/countries/v5?limit=100&offset=0',
  headers={'Authorization': 'Bearer rc_live_00cce7141b1f4dfb9d17c7e924f15ee6'}
)
data = response.json()

for data_file in data:
    countries = (data[data_file]['objects'])


# # 3.1
    
# popul_country = {}
# for country in countries:
#     if country['names']['common'] in popul_country:
#         print(f'{country['names']['common']} appears more than 1')

#     else:
#         popul_country[country['names']['common']]  = country['population']
# populs = []
# for value in popul_country.values():
#     populs.append(value)

# sorted_populs = sorted(populs)

# last_10 = sorted_populs[len(sorted_populs)-10:]

# table = f'{'Country Name':<15}   {'Population':>15}\n'
# for i in range(len(last_10)-1, -1,-1):
#     for key, value in popul_country.items():
#         if last_10[i] == value:

#             table += f'{key:<15}   {value:>15}\n'

# print('''
# =======================================================
#       TABLE OF THE 10 MOST POPULATED COUNTRIES
# =======================================================
# ''')
# print(table)


# # 3.2
# language_list = []
# for country in countries:

#     language_list.append(country['languages'])

# count = 0
# list_langs = []
# for listed in language_list:
#     for lists in listed:
#         count += 1
#         list_langs.append(lists)
# # print(count)
# # print(len(list_langs))
# languges_counts = {}
# for language in list_langs:

#     if language['name'] in languges_counts:

#         languges_counts[language['name']] += 1
#     else:
#         languges_counts[language['name']] = 1
# counts = []
# for val in languges_counts.values():
#     counts.append(val)

# sorted_counts = sorted(counts)

# most_10 = sorted_counts[len(sorted_counts)-10:]
# content_table = f'{'COUNTRY NAME': <15} {'NO. APPEARED': >15}\n'
# for i in range(len(most_10)-1,-1,-1):
#     for holder, held in languges_counts.items():
#         if most_10[i] == held:
#             content_table += f'{holder:<15} {held:<15}\n'

# print(content_table)

# 3.3
print(len(countries))


