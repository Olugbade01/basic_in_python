import re
text = "I love my mom"
dre = re.match("i love", text, re.I)
print(dre)

span = dre.span()


print(list(span))