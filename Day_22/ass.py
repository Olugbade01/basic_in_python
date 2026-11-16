import requests
import json
from bs4 import BeautifulSoup
from urllib.parse import urljoin

import time
# def url_suffix(site_url):
  
#     response = requests.get(site_url)

#     soup = BeautifulSoup(response.content, 'html.parser')
#     next_link = soup.find('li', {'class': 'next'})
#     link = next_link.find('a')
#     url_suffix = link['href']

#     return url_suffix
# def next_page_link(url):
#     suffix = url_suffix(url)
#     current_url = urljoin(url, suffix)
#     return current_url


# def data_appender(appender, appendee):

#     for book in appendee:
#         appender.append(book)
#     return appender

# Excercises 
# 1.0

        
# def scrap_pages(site_url):
#     response = requests.get(site_url, timeout=15)
#     response.raise_for_status()

#     soup = BeautifulSoup(response.content, 'html.parser')
#     titles = soup.find_all('article', {'class': 'product_pod'})

#     data = []
#     for title in titles:
#         each_h3 = title.find('h3')

#         price_tags = title.find('p', {'class': 'price_color'})
#         str_price = price_tags.text
#         ratting_tags = title.find('p', {'class': 'star-rating'}) 
#         price = float(str_price[1:])
#         rating = ratting_tags['class'][1]
#         link = each_h3.find('a')
#         book_title = link['title']
#         dict_result = {'Book Title': book_title,
#         'Price': price,
#         'Rating': rating}
#         data.append(dict_result)


#     next_button = soup.find('li', {'class': 'next'})
#     if next_button:
#         next_link = urljoin(site_url, next_button.a['href'])
#     else:
#         next_link = None
        
#     return data, next_link

# # 2.0

# url = 'https://books.toscrape.com/catalogue/page-1.html'
# counter = 0
# all_books = []
# bound_val = 60

# while url is not None and counter < bound_val:
#     try:
#         books, next_url = scrap_pages(url)
#     except requests.exceptions.RequestException as e:
#         print(f"Failed at {url}\n{e}")
#         break
    
#     all_books.extend(books)
#     url = next_url
#     counter += 1
#     print(f"At {counter} the url is \n{url}\nAnd the lenght is {len(all_books)}")  
#     time.sleep(1)  

# with open('all_books.json', 'w',ascii=False, encoding='utf-8') as file:
#     json.dump(all_books, file, indent=4)

# # 3.0

# url = 'https://quotes.toscrape.com'

# def quotes_authors(url):
#     response = requests.get(url, timeout=15)
#     response.raise_for_status()

#     soup = BeautifulSoup(response.content, 'html.parser')

#     all_quote_div = soup.find_all('div', {'class': 'quote'})
#     report = []
#     for quote in all_quote_div:
#         each_quote = quote.find('span', {'class': 'text'})
#         the_quote = each_quote.text
#         autor_link = quote.find('small', {'class': 'author'})
#         author = autor_link.text
#         tages_link_add = quote.find('div', {'class': 'tags'})
#         all_tags_links = tages_link_add.find_all('a')
#         all_tags = []
#         for each_link in all_tags_links:
#             all_tags.append(each_link.text)

#         dict_result = {
#             "Quote": the_quote,
#             "Author": author,
#             "Tags": all_tags
#         }

#         report.append(dict_result)
#     next_link = ''
#     next_button =  soup.find('li', {'class': 'next'})
    
#     if next_button:
#         next_link = urljoin(url, next_button.a['href'])
#     else:
#         next_link = None

#     return report, next_link
    

# counter = 0
# boundry = 15
# all_data = []
# while url is not None and counter < boundry:
#     try:
#         contents, next_link = quotes_authors(url)
#     except requests.exceptions.RequestException as error:
#         print(f"At {url}\n {error}")
#         break
#     counter += 1
#     all_data.extend(contents)
#     url = next_link
#     print(f'At {counter} was successful \nThe url is {url}')


    



# with open('all_data.json','w', encoding='utf-8') as file:
#     json.dump(all_data, file, ensure_ascii=False, indent=4)

# print(quotes_authors(url))

# 4.0

url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
headers = {
    "User-Agent": "LearningScraper/1.0 (https://github.com/Olugbade01/basic_in_python; abubakrakeeb07031@gmail.com)",
    "Accept-Encoding": "gzip",
}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')


# with open('wiki.html', 'r', encoding='utf-8') as file:
#     file_content = file.read()


table = soup.find('table', {'class': 'wikitable'})

for sup in table.select('sup'):
    sup.decompose()
# print("[" in table.get_text() )



str_table = table.prettify()

# print(table)

with open('real_wikitable.html', 'w', encoding='utf-8') as file:
    file.write(str_table)

sub_tags = table.find_all()




print('Work here!')