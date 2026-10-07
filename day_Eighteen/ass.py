# Excercise Level 1
# 1.0

import re
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
check = [
 'love',
 'you',
 'can',
 'what',
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
        