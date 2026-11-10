import requests
import json
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Excercises 
# 1.0
url = 'https://books.toscrape.com'

def first_20_titles(site_url):

    response = requests.get(site_url)

    soup = BeautifulSoup(response.content, 'html.parser')
    titles = soup.find_all('article', {'class': 'product_pod'})

    data = []
    for title in titles:
        each_h3 = title.find('h3')

        price_tags = title.find('p', {'class': 'price_color'})
        str_price = price_tags.text
        ratting_tags = title.find('p', {'class': 'star-rating'}) 
        price = float(str_price[1:])
        rating = ratting_tags['class'][1]
        link = each_h3.find('a')
        book_title = link['title']
        dict_result = {'Book Title': book_title,
        'Price': price,
        'Rating': rating}
        data.append(dict_result)
    return data

first_data = first_20_titles(url)
# print(first_data)
# with open('toscrap.json', 'w', encoding='utf-8') as file:
#     json.dump(first_data, file, indent=4)


# 2.0

def url_suffix(site_url):
    if str(site_url).endswith('.com'):
        response = requests.get(site_url)

        soup = BeautifulSoup(response.content, 'html.parser')
        next_link = soup.find('li', {'class': 'next'})
        link = next_link.find('a')
        url_suffix = link['href']
    return url_suffix

def find_next_20_books(site_url):

    suffix = url_suffix(site_url)
    current_url = urljoin(site_url, suffix)

    next_20 = first_20_titles(current_url)
    return next_20
mid_20 = find_next_20_books(url)
def data_appender(appender, appendee):

    for book in appendee:
        appender.append(book)
    return appender
first_40 = data_appender(first_data, mid_20)

print(first_40)