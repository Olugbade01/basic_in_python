# # Excercise Level 1
# # 1.1.1
import os
import re
import json
import csv
# dir_path = os.path.dirname(os.path.abspath('/mnt/c/Users/USER/python_basics/30-Days-Of-Python/data'))
# file_name = os.path.join(dir_path, 'data', 'obama_speech.txt')


# with open(file_name, 'r') as file:
#     file_content = file.read()  
# count = 0

# for text in file_content:
#     if text == '\n':
#         count += 1
    


# word_count = {}

# file_content = re.findall(r'\w+', file_content)
# for word in file_content:
#     word = str(word).capitalize()
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1 

# print(word_count)
# print ("The number of lines is", count)


# # 1.1.2

# michelle_file_path = os.path.dirname(os.path.abspath('/mnt/c/Users/USER/python_basics/30-Days-Of-Python/data'))
# the_path = os.path.join(michelle_file_path, 'data', 'michelle_obama_speech.txt')

# with open(the_path, 'r') as f:
#     michelle_speech = f.read()
# count_line = 0
# for text in michelle_speech:
#     if text == '\n':
#         count_line += 1

# print(f"There are {count_line} lines in Michelle's speech")

# words_pattern = re.findall(r'\w+', michelle_speech)
# word_count = {}
# for word in words_pattern:
#     word = str(word).capitalize()
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1

# print(word_count)


# # 1.1.3

# donald_path = os.path.dirname(os.path.abspath('/mnt/c/Users/USER/python_basics/30-Days-Of-Python/data'))
# d_file_path = os.path.join(donald_path, 'data', 'donald_speech.txt')

# with open(d_file_path, 'r') as fil :
#     donald_speech = fil.read()
# line_count = 0
# for char in donald_speech:
#     if char == '\n':
#         line_count += 1
# print(f"There are {line_count} in Donald's Speech")

# text_pattern = re.findall(r'\w+', donald_speech)
# text_count = {}
# for text in text_pattern:
#     text = text.capitalize()
#     if text in text_count:
#         text_count[text] += 1
#     else:

#         text_count[text] = 1

# print(text_count)


# # 1.1.4

# melina_path = os.path.dirname(os.path.abspath('/mnt/c/Users/USER/python_basics/30-Days-Of-Python/data'))
# meli_file = os.path.join(melina_path, 'data', 'melina_trump_speech.txt')

# with open(meli_file, 'r') as f:
#     melina_speech = f.read()
# counted_line = 0
# for each_word in melina_speech:
#     if each_word == '\n':
#         counted_line += 1

# print(f"There are {counted_line} lines of word in the Melina Trump Speech")


# count_words = {}

# word_only = re.findall(r'\w+', melina_speech)

# for word in word_only:
#     if word in count_words:
#         count_words[word] += 1
#     else:
#         count_words[word] = 1 
# print(count_words)


# 1.2.1

country_file = os.path.dirname(os.path.abspath('/mnt/c/Users/USER/python_basics/30-Days-Of-Python/data'))
country_path = os.path.join(country_file, 'data', 'countries_data.json')

with open(country_path, 'r') as file:
    countries = json.load(file)

# def most_spoken_lang(countries, number):
#     res = {}
#     result = []
#     language = []
    
#     for country in countries:

#         for key, value in country.items():
#             if key == 'languages':
#                 language.append(value)
#     for langs in language:
#         for lang in langs:

#             if lang in res:
#                 res[lang] += 1
#             else:
#                 res[lang] = 1
#     res_values = []
#     for vali in res.values():
#         res_values.append(vali)

#     sorted_count = sorted(res_values)

#     sorted_count = set(sorted_count)

#     for val in sorted_count:

#         for keey, valuee in res.items():
#             if val == valuee:
#                 result.append((val, keey))
#     report = []

#     for i in range(len(result)-1, len(result)-number-1, -1):
#         if number > len(result):
#             return "Number is greater than the available languages"
#         else:
#             report.append(result[i])
#     return report
# print(most_spoken_lang(countries, 10))

# # 1.3.1
# def most_populated_countries(countries, number ):
#     population = []
#     for country in countries:
#         if country['population']:
#             population.append(country['population'])

#     sorted_popul = sorted(population)
#     number_most_popul = sorted_popul[len(sorted_popul)-number:]
#     dict_country_popul = {}
#     for i in range(len(number_most_popul)-1, -1,-1):
#         for country in countries:
            
#             if country['population'] == number_most_popul[i]:
#                 dict_country_popul[country['name']] = number_most_popul[i]
#     report = []

#     for key, value in dict_country_popul.items():
#         result = {'country':key, 'population': value}
#         report.append(result)
#     return report
                
# print(most_populated_countries(countries, 3))

# Excercise Level 2

# # 2.1


# big_email_path = os.path.dirname(os.path.abspath('/mnt/c/Users/USER/python_basics/30-Days-Of-Python/data'))

# big_email_file = os.path.join(big_email_path, 'data', 'email_exchanges_big.txt')

# with open(big_email_file, 'r') as file:
#     big_email = file.read()

# pattern = re.split('Received:', big_email)

# print(pattern)

# 2.2

def find_most_common_words(file_name, number):

    path = os.path.dirname(os.path.abspath('/mnt/c/Users/USER/python_basics/30-Days-Of-Python/data'))
    file_path = os.path.join(path, 'data', file_name)

    with open(file_path, 'r') as file:
        content = file.read()

    only_words = re.findall(r'\w+', content)
    word_count = {}

    for word in only_words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    values = sorted(word_count.values())
    values = set(values)
    values = list(values)
    num_req = values[len(values)-number:]
    report = []
    for i in range(len(num_req)-1, -1,-1):
        for key, value in word_count.items():
            if value == num_req[i]:
                res = (value, key)
                report.append(res)

    return report 
# print(find_most_common_words('donald_speech.txt', 10))

# # 2.3
# # 2.3.1
# print(find_most_common_words('obama_speech.txt', 7))
# # 2.3.2
# print(find_most_common_words('michelle_obama_speech.txt', 5))
# # 2.3.3
# print(find_most_common_words('donald_speech.txt', 7))
# # 2.3.4
# print(find_most_common_words('melina_trump_speech.txt', 3))

# 2.4

# 2.5
# print(find_most_c
# ommon_words('romeo_and_juliet.txt', 10))

# 2.6

hacker_path = os.path.dirname(os.path.abspath('/mnt/c/Users/USER/python_basics/30-Days-Of-Python/data'))
file_name = os.path.join(hacker_path, 'data', 'hacker_news.csv')
count_python = 0
count_javascript = 0
word_java = 0
with open(file_name, encoding='utf-8') as file:
    file_content = csv.reader(file, delimiter=',')
    

    for words in file_content:
        for word in words:

            if word.lower().__contains__('java'):

                word_java += 1
            if word.__contains__('python') or word.__contains__('Python'):
                count_python += 1
            if word.lower().__contains__('javascript'):
                count_javascript += 1
# 2.6.1
print(f'There are {count_python} lines with python or Python in the hacker_news.csv file')

# 2.6.2

print(f'There are {count_javascript} lines with Javascript in the hacker_news.csv file')

