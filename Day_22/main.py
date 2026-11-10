import requests 
import json
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

# url = 'https://archive.ics.uci.edu/ml/datasets'

# response = requests.get(url)

# content = response.content 

# soup = BeautifulSoup(content, 'html.parser')



# print(soup.title)
# print(soup.title.get_text())
# html_format = soup.body.prettify()

# with open('site.html', 'w', encoding='utf-8') as file:
#     file.write(html_format)

# book_url = 'https://books.toscrape.com/'

# response = requests.get(book_url, timeout=10)
# # print(response.status_code)
# b_soup = BeautifulSoup(response.text, 'html.parser')

# # first_book = b_soup.find_all("article", class_="product_pod")
# # contents = b_soup.title.get_text(strip=True)
# # print(contents)
# titles = b_soup.select('article.product_pod h3 a')


# with open('titles.md', 'a', encoding='utf-8') as file:
#     for cont in titles:
#         file.write(cont['title'])

url = "https://archive.ics.uci.edu/datasets"

with sync_playwright() as:
    browser = p.chromium.launch()

    page = browser.new_page()
    page.goto(url)
    page.wait_for_selector("h2")
    html_content = page.content()
    browser.close   

soup = BeautifulSoup(html_content, 'html.parser')

