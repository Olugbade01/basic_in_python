# compN = complex(2, 3)

# print(compN)

# false = bool(0)
# print(false)


# char = chr(56)# This print the character in the index 56 on the ascii table
# print(type(char))

# maxim = min(3,47,34)# this print the minimum values of the elements 
# print(oct(300))# this print the octal values as strings
# print(maxim)
# print(char)
# print(type(format(3.1967, '.2f'))) # this correct it to 2dp as strings data type 
# print(type(round(3.1967, 2))) # this can equivalent to the above line but in float data type
# power = pow(4,2) 
# print(power)
# name = input("what is your name? ") # this request an argument from the CLI 

# print(name)




# Ass

firstname, lastname = "Abubakr", "Akeeb"
fullName = firstname + " " + lastname
country_name = "Nigeria"
city = "Iwo"
age = 27
year = 2026
is_married = True
is_true = True
is_light_on = "yes"

print(type(firstname))
print(type(lastname))
print(type(city))
print(type(is_married))
print(type(year))
print(type(is_married))

lenFistNAme = len(firstname)
lenLastName = len(lastname)
comp = lenFistNAme > lenLastName
print(comp)
number_one, number_two = 5, 4
total = number_one + number_two
diff = number_one - number_two
product = number_two * number_one
division = number_one / number_two
remainder = number_one % number_two
exp = pow(number_one, number_two)
floor_division = number_one // number_two
radius = 30
pi = 3.142 
area = round(pow(radius, 2) * pi, 2)
circum_of_circle = 2 * pi * radius
print(area, circum_of_circle, remainder, floor_division)
radius = float(input("enter the radius of the circle: "))
pi = 3.142 
area = pow(radius, 2) * pi
circum_of_circle = 2 * pi * radius
firstname = input("Enter your first name: ")
lastname = input("Enter your last name: ")
country = input("Enter your country: ")
age = input("How old are you: ")
print(area, circum_of_circle, firstname +' '+ lastname, "You are from", country)
help('len')