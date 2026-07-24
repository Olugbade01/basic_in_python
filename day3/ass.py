

base = float(input('Enter the base of the triangle: '))
height = float(input('Enter the height of the triangle: '))
area = 1/2 * base * height
area = int(area)
print(area)

# The perimeter of triangle

sideA = float(input('Enter the side A of the triangle: '))
sideB = float(input('Enter the side B of the triangle: '))
sideC = float(input('Enter the side C of the triangle: '))

peri = sideA + sideB + sideC
print(peri)

#6. 
lenght = float(input('Enter the lenght of the rectangle: '))

breath = float(input('Enter the braeth of the rectangle: '))

area_Rec = lenght * breath
peri_Rec = 2 * (lenght + breath)

print(area_Rec, peri_Rec)

# 7.

r = float(input("Input the radius of the circle: "))

pi = 3.142
area_of_circle = pi * (r ** 2) 
circum_circle = 2 * pi * r
print(area_of_circle, circum_circle)

#8.

# 9.

y1 = 2 
y2 = 10 
x1 = 2 
x2 = 6 
m = (y2 -y1)/ (x2 - x1) # slope
print("The slope is ", m)

# 10.
# 11.
'''-b +- (b2 -4ac)^1/2
first find the one iside the squaroot using the Almighty formula to solve the Quadratic equation

'''
a, b, c = 1, 6, 9

sqr = (b**2 - (4*a*c))**1/2

y1 = (-b + sqr)/ 2*a
y2 = (-b - sqr)/ 2*a

print(y1, y2)
#12. 

lenOfPy = len("python")
lenOfDrag = len("dragon")
comp = lenOfDrag > lenOfPy 
pri
nt(comp)

# 13.
onInBoth = 'on' in "python" and 'on' in "dragon"
print(onInBoth)
# 14
sentence = "I hope this course is not full of jargon"
check = "jargon" in sentence
print(check)
# 15
notinBoth = not('on' in "python" and 'on' in "dragon")
print(notinBoth)
# 16
flLenPy = float(lenOfPy)
strLenPy = str(lenOfPy)
print(flLenPy, strLenPy)
# 17.
numb = int(input("Enter the number you want to check: "))

print(numb == 0)
# 18.
fldiv = 7 // 3
intNumb = int(2.7) 
print(fldiv == intNumb)

# 19.

strNumb = '10' == 10
print(strNumb)
# 20
chNumb = "9.8" == 10 
print(chNumb)
# 21.
hour = float(input("Enter the hours of work: "))
rate = float(input("Enter the rate per hour of work: "))
weeklyPay = hour * rate
print(weeklyPay)
# 22.
years = float(input("Emter the numbers of years you've lived: "))
seconds = years * 60 * 60 * 365 * 24

print(seconds)

23. 
print(1,1,1,1,1)
print(2,1,2,4,8)
print(3,1,3,9,27)
print(4,1,4,16,64)
print(5,1, 5, 25,125)

# OR

n = 1 
m = n 
print(m, n, m*n, n**2, n**3)
m = 2 
print(m, n, m*n, m**2, m**3)
m = 3 
print(m, n, m*n, m**2, m**3)
m = 4 
print(m, n, m*n, m**2, m**3)
m = 5
print(m, n, m*n, m**2, m**3)
