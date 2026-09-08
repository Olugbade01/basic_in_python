# # Exercise Level 1

# # 1.1
# numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

# neg_and_zero = [num for num in numbers if num <= 0]
# print(neg_and_zero)

# # 1.2


# list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# single_list_of_list = [number for numb in list_of_lists for number in numb]
# print(single_list_of_list)

# # 1.3
# list_of_tupes = [(i, 1, i *1,i **2,i ** 3, i **4, i**5)for i in range(11)]

# print(list_of_tupes)

# # 1.4

# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

# lis_countries = [list(first) for second in countries for first in second]
# print(lis_countries)

# # 1.5
# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]


# dict_result = [{'country': country[0][0].upper(), 'city': country[0][1].upper()} for country in countries]

# print(dict_result)

# # 1.6 
# names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

# result = [list_names for name in names for list_names in name]
# print(result)