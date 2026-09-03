import random 
import string


# printable = string.printable

# count = 0

# space = []


# print(printable, 'It stops here')
# print(len(printable))  # This prints 100
# for ind, char in enumerate(printable):

#     if char.isspace():

#         space.append(ind)

#         count += 1

# print(count, space)


# printable = printable.strip()
# print(printable, "It stops here!")
# print(len(printable)) # While this one prints 94

# # Level 1
# # 1.1
# def random_user_id():

#     password_chars = string.ascii_letters


#     password_chars = list(password_chars)

#     digits = string.digits
#     digits = list(digits)


#     password_chars = password_chars.__add__(digits)


#     pass_choices = random.choices(password_chars, k = 6)

#     password = ""
#     password = password.join(pass_choices)
#     return password



# print(random_user_id())

# # 1.2
# def user_id_gen_by_user(password_len, numb_of_password):
#     result = ""


#     for i in range(1, numb_of_password + 1):
#         pass_letters = string.ascii_letters

#         pass_digit = string.digits

#         pass_letters = list(pass_letters)
#         pass_digit = list(pass_digit)

#         pass_chars = pass_letters.__add__(pass_digit)

#         list_pass_gen = random.choices(pass_chars, k = password_len)

#         password = "".join(list_pass_gen)

#         result += password + "\n"

#     return result
# print(user_id_gen_by_user(16,5))

# # 1.3

# def rgb_color_gen():

#     result = []

#     for i in range(1,4):

#         numbs = random.randint(0,255)
#         result.append(numbs)


#     result = tuple(result)
#     result = str(result)
#     result = 'rgb'.__add__(result)
#     return result


# print(rgb_color_gen())


# # Level 2
# # 2.1
# def list_of_hexa_colors(numbs):
    

#     list_of_color_code = []

#     for i in range(1, numbs + 1 ):
#         color_code = "#"
#         hexa_alpha = "abcdef"

#         color_numbers = string.digits
        
#         # return  color_numbers
#         hexa_color_char = hexa_alpha.__add__(color_numbers)
        
#         list_code = random.choices(hexa_color_char, k = 6)
#         code = "".join(list_code)
#         color_code = color_code.__add__(code)

#         list_of_color_code.append(color_code)

#     return list_of_color_code



# print(list_of_hexa_colors(5))

# # 2.2

# def list_of_rgb_colors(number):

#     list_of_rgb = []

#     for x in range(1, number + 1):

#         rgb_color_codes = []

#         for i in range(1, 4):
#             color_numbers = random.randint(0, 255)
#             rgb_color_codes.append(color_numbers)
        
#         color_codes = tuple(rgb_color_codes)
#         color_codes = str(color_codes)

#         the_rgb_code = 'rgb'.__add__(color_codes)

#         list_of_rgb.append(the_rgb_code)
#     return list_of_rgb
# print(list_of_rgb_colors(2))

# # 2.3
# def generate_colors(type, numbers):

#     result = []
#     if type == 'hexa':

#         for i in range(1, numbers + 1):
#             color_codes = "#"

#             digits_codes = string.digits
#             hexa_codes = 'abcdef'
#             all_codes = hexa_codes.__add__(digits_codes)

#             alpha_num_codes = random.choices(all_codes, k = 6)

#             the_codes = ''.join(alpha_num_codes)
#             color_codes = color_codes.__add__(the_codes)

#             result.append(color_codes)
    

#     if type == 'rgb':

#         for i in range(1, numbers +1 ):

#             the_code = []
#             for x in range(1, 4):

#                 codes_digits = random.randint(0,255)

#                 the_code.append(codes_digits)

#             tuple_code = tuple(the_code)

#             str_code = str(tuple_code)
#             color_codes = 'rgb'.__add__(str_code)

#             result.append(color_codes)
#     return result

# print(generate_colors('rgb', 3))


# # Level 3
# # 3.1

# def shuffle_list(listed_items):

#     listed_items = set(listed_items)

#     return list(listed_items)

# print(shuffle_list(['a', 'b', 'c', 10]))

# 3.2
def array_of_seven_elements():
    

    numb = string.digits
        
    numbers = random.choices(numb, k = 7)
    
        

    return numbers

print(array_of_seven_elements())