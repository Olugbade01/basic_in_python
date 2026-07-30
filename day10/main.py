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

numb = range(0, 30)
for i in numb:
    if i % 2 == 0:
        if numb == 4 or numb == 16:
            print(f'%d is a square number'%(numb))
        else:
            print(f'%d is not a square number'%(numb))
    else:
        print(f'%d is where the iterations stops'%(numb))