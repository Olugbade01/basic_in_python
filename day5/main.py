# import keyword

# print(keyword.iskeyword("del"))

mklist = list() 
mklist = ['hello', 'seen', 'let']
mklist[2] = 'how'
# print(mklist)
mklist.insert(3, 'World')
mklist.remove('seen')
mklist.append('dress')
lis = mklist.copy()
num = mklist.count('dress')
# print(num)
mklist.extend('dress')
# print(mklist[-2])
numm = mklist.index('how')
# pop = mklist.pop(1)
# print(pop)
# mklist.clear()
# mklist.reverse()
mklist.sort()
print(mklist)
# print(lis)
# print(numm)
# print(len(mklist))
# mktuple = tuple()
# mktuple = ['hello', 547, 500, True]
# mktuple[-3] = False
# print(mktuple)