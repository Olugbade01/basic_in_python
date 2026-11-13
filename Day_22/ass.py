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

url = 'https://quotes.toscrape.com'

def quotes_authors(url):
    response = requests.get(url, timeout=15)

    soup = BeautifulSoup(response.content, 'html.parser')
    contents = soup.body.prettify()
    return contents

with open('check.html','w', encoding='utf-8') as file:
    file.write(quotes_authors(url))


print('Work here!')

