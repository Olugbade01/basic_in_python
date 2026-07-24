lenght = input("Input the lenght of the rectangle: ")
breath = input("Input the breath of the rectangle: ")
fllen = float(lenght)
flbreath = float(breath)

area_of_rectangle = fllen * flbreath 

print(area_of_rectangle)

# Now calculating the area of a circle with r as the radius 

r = float(input("Input the radius of the circle: "))

pi = 3.142
area_of_circle = pi * (r ** 2) 
print(area_of_circle)

# Calculating the acceleration of a moving object 

diplacement = float(input('enter the displacement of the object: '))
time = float(input('Enter the timme: '))

acceleration = diplacement * time
print('The acceleration is ', acceleration, "m/s^2")

#The use of mathematical operators <,>,==,!=,>= and <= returns True or False depending on the correctness of the operator

print(4>3) # this prints true 
print(3>10) #THis prints false 
print(True == True) # This prints true 
print(15 == 14) # This print False 
print(len("Friend") <= len("Mango")) #This prints False 

# other operators in Python that returns True or False are is, is not, in and not in, if the statement in the left and right satisfies the condition between or not respectively 

print(5 is (len("Guard"))) # This is true 
print(7 is not (len("Branded"))) # This returns False
print(5 is 5)

print(3 in [1, 2, 3, 4])
print(6 not in [6, 7, 8,9, 10]) # This returns False 

print('b' in 'Baboon') #This prints True

print('b' in 'Black') # This prints False 


# Other operators like and, or and not 

print(3 > 10 and 2 < 6) #This returns because the first is not true 
print(3 > 10 or 2 < 6) # This returns True because either of the 2 is true 

print(not(3 > 10 and 2 < 6)) # This returns True because either of the two is true
print(not(3 < 10 and 2 < 6)) # This returns False because both statements are true

print(not(3 > 10 or 2 < 6)) #This also returns False because either of the 2 statements is true 

print(not(3 < 10 or 2 < 6)) #This alse returns False because either or both is true 

print(not(3 >= 10 or 2 >= 6)) # This returns the True because neither of the 2 is true

print(not True) #This negate the condition and prints False 

print(not not not True) #This print False
print(not not False) # This us False 



