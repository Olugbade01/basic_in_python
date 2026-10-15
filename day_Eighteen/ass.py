# Excercise Level 1
# 1.0

import re
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
check = [
 'love',
 'you',
 'can',
 'what',# # # Excercise Level 1
# # # 1.1
# # import re
# # paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
# # splitted_paragraph = re.findall(r'\w+', paragraph)

# # count_words = {}
# # for word in splitted_paragraph:
# #     word = word.lower()    
# #     if word in count_words.keys():
# #         count_words[word] += 1

# #     else:
# #         count_words[word] = 1  

# # list_count = []
# # for key, value in count_words.items():
# #     tuple_count = (value, key)
# #     list_count.append(tuple_count)
# # print(list_count)

# # # 1.2

# # points = ['-12', '-4', '-3', '-1', '0', '4', '8']

# # def int_checker(number):
# #     try:
# #         number = int(number)
# #         return number
# #     except:
# #         return "Not a valid number!"


# # int_numbs = map(int_checker, points)
# # list_numbs = list(int_numbs)
# # distance = max(list_numbs) - min(list_numbs)
# # print(distance)

# # # 2.1
# import re
# # def is_valid_var(variable):

# #     if re.match(r'\d', variable[0]):
# #         return False

# #     else:
# #         if re.match(r'[a-zA-Z]\w*$', variable) :
# #             return True
# #         else:
# #             return False

# # print(is_valid_var('first-name'))

# # 3.1
# sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

# clean_text = re.sub(r'[%@#?$&;!]', '', sentence)

# print(clean_text)
 'teaching',
 'not',
 'else',
 'do',
 'I',
 'which',
 'to',
 'the',
 'something',
 'if',
 'give',
 'develop',
 'capabilities',
 'application',
 'an',
 'all',
 'Python',
 'If'
]

splitted_paragraph = re.split(' ', paragraph)
def it_matched(word):
        
