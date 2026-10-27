# # Excercise Level 1
# # # 1.1
# import urllib.request
# import requests
# import re
# import os
# # option 1 

# site_url = 'https://www.gutenberg.org/cache/epub/5933/pg5933-images.html'
# with urllib.request.urlopen(site_url) as file:
#     raed_ = file.read()
# # print(raed_)
# # Option 2
# response = requests.get(site_url)

# response = response.text

# text_only = re.findall(r'\w+', response)

# word_count = {

# }

# for word in text_only:
#     word = str(word).capitalize()
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
# values = []
# for val in word_count.values():
#     values.append(val)

# sorted_val = sorted(values)
# last_10 = sorted_val[len(sorted_val)-10:]
# report = []
# for i in range(len(last_10)-1, -1, -1):
#     for key, value in word_count.items():
#         if value == last_10[i]:
#             report.append((key, value))
# print(report)


# # 1.2
# url_api = 'https://api.thecatapi.com/v1/breeds'

# api_key = os.environ.get("CAT_API_KEY")

# headers = {"x-api-key": api_key}

# api_response = requests.get(url_api, headers=headers)

# print(api_response.status_code)

# print(api_response.te)