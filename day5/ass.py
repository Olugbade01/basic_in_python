# # # mklist = list()
# # # newlist = ['who', 'are', 'you', 'today', 'family', 600, 'school']
# # # # 3.
# # # print(len(newlist))
# # # # 4.
# # # print(newlist[0], newlist[3], newlist[6])
# # # print(newlist[::3])
# # # # 5.
# # # mixed_data_types = ['Abubakr', 20, 5.9, 'single', 'GRA']
# # # # 6.
# # it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# # # # 7.
# # # print(mixed_data_types)
# # # print(it_companies)
# # # # 8.
# # # print(len(it_companies))
# # # # 9.
# # # print(it_companies[::3])
# # # # 10.

# # # it_companies[3] = 'Linux'
# # # # print(it_companies)
# # # # # 11.
# # # print(it_companies.__add__(['Window']))
# # # # 12.
# # # it_companies.insert(4, 'London')
# # # print(it_companies)
# # # # 13.
# # # it_companies[3] = it_companies[3].upper()
# # # print(it_companies)
# # # # 14.
# # # print('# '.join(it_companies))
# # # # 15.
# # # print(it_companies.__contains__('IBM'))
# # # # 16.
# # it_companies.sort()
# # print(it_companies)
# # # 17.

# # it_companies.reverse()
# # print(it_companies)
# # 18.
# # print(it_companies[:3])
# # # 19.
# # print(it_companies[len(it_companies)-3:])
# # # 20.
# # print(it_companies[int(len(it_companies)/2)])
# # # 21.
# # it_companies.remove('Oracle')
# # print(it_companies)
# # # 22.
# # it_companies.pop(int(len(it_companies)/2))
# # print(it_companies)
# # # 23.
# # it_companies.pop(int(len(it_companies)-1))
# # print(it_companies)
# # # 24.
# # it_companies.clear()
# # print(it_companies)
# # # 25.
# # del it_companies
# # # print(it_companies)

# # front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# # back_end = ['Node','Express', 'MongoDB']

# # front_end.__iadd__(back_end)
# # print(front_end)
# # # 27.
# # full_stack = front_end.copy()
# # print(full_stack)


# # Exercise 2 

# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# ages.sort()
# print(ages)
# summation = max(ages) + min(ages)
# print(summation)
# # average = int((ages[int(len(ages)/2)] + ages[int(len(ages)/2)-1])/2)
# # OR
# median = int((ages[4] + ages[5])/2)
# print(median)

# average = sum(ages)/ len(ages)
# print(average)

# drange = max(ages) - max(ages)
# print(drange)

# min(ages) -  average

# print((min(ages) -  average).__abs__())

# countries = [
#   'Afghanistan',
#   'Albania',
#   'Algeria',
#   'Andorra',
#   'Angola',
#   'Antigua and Barbuda',
#   'Argentina',
#   'Armenia',
#   'Australia',
#   'Austria',
#   'Azerbaijan',
#   'Bahamas',
#   'Bahrain',
#   'Bangladesh',
#   'Barbados',
#   'Belarus',
#   'Belgium',
#   'Belize',
#   'Benin',
#   'Bhutan',
#   'Bolivia',
#   'Bosnia and Herzegovina',
#   'Botswana',
#   'Brazil',
#   'Brunei',
#   'Bulgaria',
#   'Burkina Faso',
#   'Burundi',
#   'Cabo Verde',
#   'Cambodia',
#   'Cameroon',
#   'Canada',
#   'Central African Republic',
#   'Chad',
#   'Chile',
#   'China',
#   'Colombia',
#   'Comoros',
#   'Congo, Democratic Republic of the',
#   'Congo, Republic of the',
#   'Costa Rica',
#   "Côte d'Ivoire",
#   'Croatia',
#   'Cuba',
#   'Cyprus',
#   'Czech Republic',
#   'Denmark',
#   'Djibouti',
#   'Dominica',
#   'Dominican Republic',
#   'East Timor (Timor-Leste)',
#   'Ecuador',
#   'Egypt',
#   'El Salvador',
#   'Equatorial Guinea',
#   'Eritrea',
#   'Estonia',
#   'Eswatini',
#   'Ethiopia',
#   'Fiji',
#   'Finland',
#   'France',
#   'Gabon',
#   'Gambia',
#   'Georgia',
#   'Germany',
#   'Ghana',
#   'Greece',
#   'Grenada',
#   'Guatemala',
#   'Guinea',
#   'Guinea-Bissau',
#   'Guyana',
#   'Haiti',
#   'Honduras',
#   'Hungary',
#   'Iceland',
#   'India',
#   'Indonesia',
#   'Iran',
#   'Iraq',
#   'Ireland',
#   'Israel',
#   'Italy',
#   'Jamaica',
#   'Japan',
#   'Jordan',
#   'Kazakhstan',
#   'Kenya',
#   'Kiribati',
#   'Korea, North',
#   'Korea, South',
#   'Kuwait',
#   'Kyrgyzstan',
#   'Laos',
#   'Latvia',
#   'Lebanon',
#   'Lesotho',
#   'Liberia',
#   'Libya',
#   'Liechtenstein',
#   'Lithuania',
#   'Luxembourg',
#   'Madagascar',
#   'Malawi',
#   'Malaysia',
#   'Maldives',
#   'Mali',
#   'Malta',
#   'Marshall Islands',
#   'Mauritania',
#   'Mauritius',
#   'Mexico',
#   'Micronesia',
#   'Moldova',
#   'Monaco',
#   'Mongolia',
#   'Montenegro',
#   'Morocco',
#   'Mozambique',
#   'Myanmar',
#   'Namibia',
#   'Nauru',
#   'Nepal',
#   'Netherlands',
#   'New Zealand',
#   'Nicaragua',
#   'Niger',
#   'Nigeria',
#   'North Macedonia',
#   'Norway',
#   'Oman',
#   'Pakistan',
#   'Palau',
#   'Palestine',
#   'Panama',
#   'Papua New Guinea',
#   'Paraguay',
#   'Peru',
#   'Philippines',
#   'Poland',
#   'Portugal',
#   'Qatar',
#   'Romania',
#   'Russia',
#   'Rwanda',
#   'Saint Kitts and Nevis',
#   'Saint Lucia',
#   'Saint Vincent and the Grenadines',
#   'Samoa',
#   'San Marino',
#   'Sao Tome and Principe',
#   'Saudi Arabia',
#   'Senegal',
#   'Serbia',
#   'Seychelles',
#   'Sierra Leone',
#   'Singapore',
#   'Slovakia',
#   'Slovenia',
#   'Solomon Islands',
#   'Somalia',
#   'South Africa',
#   'South Sudan',
#   'Spain',
#   'Sri Lanka',
#   'Sudan',
#   'Suriname',
#   'Sweden',
#   'Switzerland',
#   'Syria',
#   'Tajikistan',
#   'Tanzania',
#   'Thailand',
#   'Togo',
#   'Tonga',
#   'Trinidad and Tobago',
#   'Tunisia',
#   'Turkey',
#   'Turkmenistan',
#   'Tuvalu',
#   'Uganda',
#   'Ukraine',
#   'United Arab Emirates',
#   'United Kingdom',
#   'United States',
#   'Uruguay',
#   'Uzbekistan',
#   'Vanuatu',
#   'Vatican City',
#   'Venezuela',
#   'Vietnam',
#   'Yemen',
#   'Zambia',
#   'Zimbabwe'
# ]
# print(len(countries))
# middleCountry = int(len(countries)/2)
# print(countries[middleCountry])
# midIndex = int(len(countries)/2) + 1
# first_half = countries[:midIndex]
# last_half = countries[midIndex:]
# print(first_half)
# print(len(first_half), len(last_half))
# print(last_half)

packed = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

first, second, third, *others = packed 
print(first)
print(others)