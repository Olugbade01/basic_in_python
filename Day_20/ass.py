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

        

url_api = 'https://api.thecatapi.com/v1/breeds'

# the_api_key = live_99PsER2UvaAz0YPhs6CbZ1ZxkSMaF7fUbFiNE8ArP5ijKZoFqvTV7WRR6qhiFcjj

api_key = os.environ.get("CAT_API_KEY")



headers = {"x-api-key": api_key}

api_response = requests.get(url_api, headers=headers)

print(api_response.status_code)

result = api_response.json()

numbs = []
for each_bread in result:

    numbs.append(each_bread['weight']['metric'].split('-'))
list_floated_numbs = []       
for num in numbs:
    if len(num) == 2:
        converted = convet_to_float(num)
    else:
        continue

    list_floated_numbs.append(converted)
   
# print(list_floated_numbs)
averages = []
for floated_number in list_floated_numbs:
    averages.append(average_calculator(floated_number))

# print(averages)
# # 2.1.1
# print(min(averages))
# # 2.1.2
# print(max(averages))
# 2.1.3
def median_of_averages(list_averages):
    list_numbers = sorted(list_averages)
with open('result.json', 'w') as file:
    json.dump(result, file, indent=4)