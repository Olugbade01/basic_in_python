# #  For Loop and While Loop
# i = 0
# while i < 10:
#     print(i)
#     i = i +1
#     # This prints the number from 0 to 9
#     # but if preceeded with else conditons it execute on the supposed last iteration
# else:
#     print(i) # This only print when i is exactly 10

# #  we use break to get out of the loop to prevet an infinit loop or use the point at which the loop is, i.e every other iteration beyound is not required.

# numb = 1
# while numb < 100:
#     # numb +=  numb
#     numb += 1
#     # numb += 0
#     if numb % 2 == 0:
#         if numb ** (1/2) == 2 or numb ** (1/2) == 4 or numb ** (1/2) == 6 or numb ** (1/2) == 8 or numb ** (1/2) == 10:
#             print(f'%d is a square number'%(numb))
#         else:
#             print(f'%d is not a square number'%(numb))
#     elif numb ** (1/2) == 3 or numb ** (1/2) == 5 or numb ** (1/2) == 7 or numb ** (1/2) == 9:
#         print(f'%d is a square number'%(numb))
#     else:
#         print(f'%d is an odd number'%(numb))

# else:
#     print(f'%d is where the iterations stops'%(numb))

# # For Loop !!!

# lang = 'Python'
# count = 0 
# for letters in lang:
#     count += 1
# print(count)

# text = 'Who are you to question the authority.'
# count = 0
# for a in text:
#     if a == ' ':
#         count += 1
# print(f'We have %d spaces in the text'%(count))