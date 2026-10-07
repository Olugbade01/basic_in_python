import re
# text = "I love my mom"
# dre = re.match("i love", text, re.I)
# print(dre)

# span = dre.span()


# print(list(span))

# text = '''Python is the First most beautiful language that a human being has ever created.
# I recommend python for a first programming language Firstlang'''

# search = re.search('first', text, re.I)

# print(search)
# search_all = re.findall('[fF]irst', text)

# print(search_all)
# search_all = re.findall('First|first ', text)
# print(search_all)

# replace_match = re.sub('python|Python', "Javascript", text, re.I)
# print(replace_match)

# replace_match = re.sub('[Pp]ython', "Javascript", text)
# print(replace_match)


# txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
# T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
# I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
# D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''


# clean_txt = re.sub('%', '', txt)

# print(clean_txt)

# SPLITTING 

# txt = '''I am teacher and  I love teaching.
# There is nothing as rewarding as educating and empowering people.
# I found teaching more interesting than any other jobs.
# Does this motivate you to be a teacher?'''

# print(re.split('\n', txt))

# REGEX_PATTERNS

regex_pattern = r'apple'
txt = 'an Apple and banana are fruits. ? An 155 old Day may haycliche 10 says an 56 apple a day a doctor way has been anyone replaced by a banana a day keeps the doctor far far away. pan'
reg_path = r'[aA-mM]ay'
digit = r'\d'
non_digit = r'\D'
# print(re.findall(regex_pattern, txt, re.I))
# print(re.findall(reg_path, txt))
# print(re.findall(digit, txt)) # Digit
# print(re.findall(non_digit, txt, re.I)) #Non digit
strt_an = r'^an'
end_with = r'an$'
appearances = r'[a].?'
char_of_num = r'\d{3}'
one_word = r'\W'
not_abc = r'[^a-zA-Z]+'
print(re.findall(not_abc, txt))