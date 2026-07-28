# Excercise One 

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
# print(len(it_companies))
# it_companies.add('Twitter')
# print(it_companies)
# others = {'Linux', 'IHS', 'Globacom'}
# it_companies.update(others)
# print(len(it_companies))
# it_companies.discard('Locust') #This doesnt trow error 
# # it_companies.remove('Locust') #this trows an error
# print(len(it_companies))
# print(it_companies)

# # Excercise 2 
# A.update(B)
# print(A)
# A.intersection(B)
# print(A)
# print(A.issubset(B))
# print(A.isdisjoint(B))
# C = A.union(B)
# D = B.union(A)
# F = C.intersection(D)
# print(F)
# A.symmetric_difference(B)
# print(A)

del (A, B)

# Excercise 3 

set_age = set(age) # Set is a collection a well defined element can not be replaced but can be increased 
print(set_age)
print(len(set_age), len(age)) # the lenght of the list is begger than sets' because sets are distinct object 

tuple_age = tuple(age) # Tuple is imutable list  
print(tuple_age)
str_age = str(age) # string is atext like data type written inside coatation 
print(str_age)
# And set is a collections of distinct element it imutatb
print(age) 