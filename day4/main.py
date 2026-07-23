# # 21.
# hour = float(input("Enter the hours of work: "))
# rate = float(input("Enter the rate per hour of work: "))
# weeklyPay = hour * rate
# print(weeklyPay)
# # 22.
# years = float(input("Emter the numbers of years you've lived: "))
# seconds = years * 60 * 60 * 365 * 24

# print(seconds)

# 23. 
# print(1,1,1,1,1)
# print(2,1,2,4,8)
# print(3,1,3,9,27)
# print(4,1,4,16,64)
# print(5,1, 5, 25,125)

# n = 1 
# m = n 
# print(m, n, m*n, n**2, n**3)
# m = 2 
# print(m, n, m*n, m**2, m**3)
# m = 3 
# print(m, n, m*n, m**2, m**3)
# m = 4 
# print(m, n, m*n, m**2, m**3)
# m = 5
# print(m, n, m*n, m**2, m**3)



# strn = '''Hello my brother how are you doing, are you doing ookay there this morning 
# I have to tell you about my progress with python lately
# Things are getting a bit more interesting'''
# chrc = 'how' in strn
# print(chrc)

# print('Table of Content')
# print('Day\tData-Type\tExamples')
# print('Day 1\tString\t"Hello World!"')
# print('Day 2\tBoolean\tTrue')
# print('Day 3\tIntegers\t460\nDay 4\tFloat\t4.60')
# print('This is called the double coatation mark \'')
# dress = "native"
# color = "red"
# attire = "Yoruba"
# numbers = 20
# print("I need %d %s %ss as Aso-Ebi for the wedding it has to be in %s full regalia" %(numbers,color,dress,attire) )
# num1 = 30
# num2 = 7

# print(f'The floor division is {num1} // {num2} = {num1//num2}')
# print('The remainder from the division is {}'.format(num1%num2))
# print('The division to 3 D.P is {:.3f}'.format(num1 / num2))
# # Unpacking 

# name = "Moridiyah"
# a,b,c,d,e,f,g,h,i = name
# print(a,h,c,d,h,a)

# # Reversing a string 

# word = "Dressing"
# print(word[::-1])
# print(word[::2])
# print(word[:2])
# print(word[::1])
# print(word[::3])

strText = "My name is Abubakr Busayo and my sur\tname is dres \u00df Akeeb is letter a"
char = "A"
unicode = "\x0f"
suscript = "\u00ff"
frac = "1/2"
sltext = ["Hello", 'My', "People"]
strWord = 'things fall apart'
# print(strText.capitalize())
# print(strText.casefold())
# print(strText.center(100))
# print(strText.expandtabs(30))
# print(strText.rfind('y'))
# print(strText)
# print(strText.isalnum())
# print(char.isdecimal())
# print(unicode)
# print(suscript.isprintable())
# print(frac.isprintable())
print('_'.join(sltext))
print(strWord.title())