# 30 Days Of Python: Day 22 - Web Scraping

[<< Day 21](../21_Day_Classes_and_objects/21_classes_and_objects.md) | [Day 23 >>](../23_Day_Virtual_environment/23_virtual_environment.md)

- [Day 22](#day-22)
  - [What is web scraping](#what-is-web-scraping)
  - [Before you scrape: be a good citizen](#before-you-scrape-be-a-good-citizen)
  - [Setup](#setup)
  - [Step 1: Fetch a page](#step-1-fetch-a-page)
  - [Step 2: Parse it with BeautifulSoup](#step-2-parse-it-with-beautifulsoup)
  - [Step 3: Extract a table](#step-3-extract-a-table)
  - [Step 4: Save the data as JSON](#step-4-save-the-data-as-json)
  - [The big modern problem: JavaScript-rendered pages](#the-big-modern-problem-javascript-rendered-pages)
  - [Choosing the right tool](#choosing-the-right-tool)
  - [Exercises: Day 22](#exercises-day-22)

# Day 22

## What is web scraping

The internet holds a huge amount of data, but not all of it comes with a download button or an API. Web scraping is the process of extracting data from websites and storing it locally, in a file or a database.

In this lesson we use two packages:

- `requests` (or `httpx`) to download a page
- `beautifulsoup4` to parse the HTML and pull out the pieces we want

BeautifulSoup is still the standard HTML parser in Python. What has changed is that many modern sites load their data with JavaScript, so downloading the HTML is no longer always enough. We cover that later in this lesson.

To scrape well you need a basic understanding of HTML tags, attributes, classes and ids. You target content by those.

## Before you scrape: be a good citizen

1. **Check `robots.txt`.** Visit `https://example.com/robots.txt` to see what the site allows crawlers to access.
2. **Read the terms of use.** Some sites forbid scraping.
3. **Prefer an official API or download** if one exists. It is faster, more stable and legal to use.
4. **Be gentle.** Add a delay between requests (`time.sleep(1)`) and never hammer a server with rapid-fire requests.
5. **Identify yourself.** Send a `User-Agent` header. Some sites, including Wikipedia, block the default one used by `requests`.

## Setup

Create a project with [uv](https://docs.astral.sh/uv/) and add the packages:

```sh
uv init day22-scraping
cd day22-scraping
uv add requests beautifulsoup4
```

Run your scripts with:

```sh
uv run main.py
```

If you prefer the classic way, `python -m venv .venv`, activate it, then `pip install requests beautifulsoup4` works too.

## Step 1: Fetch a page

We will practise on [books.toscrape.com](https://books.toscrape.com), a site built for learning scraping. It serves plain HTML, so it works with `requests` directly.

```py
import requests

url = "https://books.toscrape.com/"
headers = {"User-Agent": "learning-python-scraper/1.0"}

response = requests.get(url, headers=headers, timeout=10)
response.raise_for_status()   # raises an error for 4xx / 5xx responses

print(response.status_code)   # 200 means success
```

```sh
200
```

Two small habits worth building:

- `timeout=10` stops your script hanging forever if the server does not answer.
- `raise_for_status()` fails loudly instead of letting you parse an error page by accident.

## Step 2: Parse it with BeautifulSoup

```py
import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
headers = {"User-Agent": "learning-python-scraper/1.0"}

response = requests.get(url, headers=headers, timeout=10)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.get_text(strip=True))
```

Use `response.text` (decoded text) when parsing, rather than `response.content` (raw bytes), unless you have a reason to handle encoding yourself.

Now find elements. The three methods you will use most:

```py
# first match only (returns None if nothing matches)
first_book = soup.find("article", class_="product_pod")

# all matches (returns a list, empty if nothing matches)
books = soup.find_all("article", class_="product_pod")

# CSS selectors, often the cleanest option
titles = soup.select("article.product_pod h3 a")
```

Extract data from each book:

```py
data = []
for book in books:
    title = book.h3.a["title"]               # attribute access
    price = book.select_one(".price_color").get_text(strip=True)
    link = book.h3.a["href"]
    data.append({"title": title, "price": price, "link": link})

print(data[:3])
```

Useful tools:

| Task | Code |
|---|---|
| Get text | `tag.get_text(strip=True)` |
| Get an attribute | `tag["href"]` or `tag.get("href")` |
| Filter by attribute | `soup.find_all("table", {"cellpadding": "3"})` |
| CSS selector | `soup.select("div.card > a")` |
| Safe lookup | `tag.get("href", "")` avoids a `KeyError` |

`{"cellpadding": "3"}` is an old HTML attribute used here as a filter. Newer pages normally use `class` or `id` instead.

## Step 3: Extract a table

Tables appear on many pages, Wikipedia especially. Here is how to read a table row by row:

```py
table = soup.find("table")
rows = table.find_all("tr")

header = [th.get_text(strip=True) for th in rows[0].find_all("th")]

records = []
for row in rows[1:]:
    cells = [td.get_text(strip=True) for td in row.find_all("td")]
    if cells:
        records.append(dict(zip(header, cells)))
```

**Shortcut with pandas.** If the table is in the raw HTML, one line does the job:

```py
import pandas as pd

tables = pd.read_html("https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States")
print(len(tables))
print(tables[0].head())
```

Install the extras first with `uv add pandas lxml`. Some sites reject the default pandas request, so you may need to download the page with `requests` (with a `User-Agent`) and pass `response.text` to `pd.read_html` using `io.StringIO`.

## Step 4: Save the data as JSON

```py
import json

with open("books.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
```

`encoding="utf-8"` and `ensure_ascii=False` keep special characters readable.

## The big modern problem: JavaScript-rendered pages

Try this on a page and you may find nothing in your results:

```py
soup.find_all("table")   # []
```

The reason is that `requests` only downloads the HTML the server sends. It does not run JavaScript. Many modern sites send a nearly empty page and then use JavaScript to load the data, so BeautifulSoup never sees it.

The UCI Machine Learning Repository is a good example. The old lesson used `https://archive.ics.uci.edu/ml/datasets.php` with `cellpadding="3"` tables. The site has since been redesigned (the list now lives at `https://archive.ics.uci.edu/datasets`) and is built with JavaScript, so that old code returns nothing.

### How to tell

1. Right-click the page in your browser and choose **View page source** (not Inspect). If the data you see on screen is missing from the source, JavaScript is loading it.
2. Or check in code: `print(len(soup.find_all("table")))` returns `0`.

### What to do about it, in order of preference

**1. Use an official package or API.** For UCI, the maintained package is `ucimlrepo`:

```sh
uv add ucimlrepo
```

```py
from ucimlrepo import fetch_ucirepo

iris = fetch_ucirepo(id=53)

print(iris.data.features.head())
print(iris.metadata)
```

**2. Find the hidden API the page calls.** Open the browser developer tools, go to the **Network** tab, filter by **Fetch/XHR**, then reload the page. You will often see a request that returns the data as JSON. Call it directly:

```py
import requests

api_url = "PASTE_THE_URL_YOU_FOUND_HERE"
data = requests.get(api_url, timeout=10).json()
```

No HTML parsing is needed, and it is faster and more stable than scraping.

**3. Drive a real browser with Playwright.** It runs the JavaScript for you:

```sh
uv add playwright
uv run playwright install
```

```py
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://archive.ics.uci.edu/datasets")
    page.wait_for_selector("h2")        # wait for content to appear
    html = page.content()
    browser.close()

soup = BeautifulSoup(html, "html.parser")
```

Notice that BeautifulSoup is still used at the end. Playwright gets the rendered page, and BeautifulSoup extracts from it.

## Choosing the right tool

| Situation | Tool |
|---|---|
| Static HTML page | `requests` + BeautifulSoup |
| Static HTML table | `pandas.read_html` |
| Data loaded by JavaScript, API visible | Call the# 30 Days Of Python: Day 22 - Web Scraping

[<< Day 21](../21_Day_Classes_and_objects/21_classes_and_objects.md) | [Day 23 >>](../23_Day_Virtual_environment/23_virtual_environment.md)

- [Day 22](#day-22)
  - [What is web scraping](#what-is-web-scraping)
  - [Before you scrape: be a good citizen](#before-you-scrape-be-a-good-citizen)
  - [Setup](#setup)
  - [Step 1: Fetch a page](#step-1-fetch-a-page)
  - [Step 2: Parse it with BeautifulSoup](#step-2-parse-it-with-beautifulsoup)
  - [Step 3: Extract a table](#step-3-extract-a-table)
  - [Step 4: Save the data as JSON](#step-4-save-the-data-as-json)
  - [The big modern problem: JavaScript-rendered pages](#the-big-modern-problem-javascript-rendered-pages)
  - [Choosing the right tool](#choosing-the-right-tool)
  - [Exercises: Day 22](#exercises-day-22)

# Day 22

## What is web scraping

The internet holds a huge amount of data, but not all of it comes with a download button or an API. Web scraping is the process of extracting data from websites and storing it locally, in a file or a database.

In this lesson we use two packages:

- `requests` (or `httpx`) to download a page
- `beautifulsoup4` to parse the HTML and pull out the pieces we want

BeautifulSoup is still the standard HTML parser in Python. What has changed is that many modern sites load their data with JavaScript, so downloading the HTML is no longer always enough. We cover that later in this lesson.

To scrape well you need a basic understanding of HTML tags, attributes, classes and ids. You target content by those.

## Before you scrape: be a good citizen

1. **Check `robots.txt`.** Visit `https://example.com/robots.txt` to see what the site allows crawlers to access.
2. **Read the terms of use.** Some sites forbid scraping.
3. **Prefer an official API or download** if one exists. It is faster, more stable and legal to use.
4. **Be gentle.** Add a delay between requests (`time.sleep(1)`) and never hammer a server with rapid-fire requests.
5. **Identify yourself.** Send a `User-Agent` header. Some sites, including Wikipedia, block the default one used by `requests`.

## Setup

Create a project with [uv](https://docs.astral.sh/uv/) and add the packages:

```sh
uv init day22-scraping
cd day22-scraping
uv add requests beautifulsoup4
```

Run your scripts with:

```sh
uv run main.py
```

If you prefer the classic way, `python -m venv .venv`, activate it, then `pip install requests beautifulsoup4` works too.

## Step 1: Fetch a page

We will practise on [books.toscrape.com](https://books.toscrape.com), a site built for learning scraping. It serves plain HTML, so it works with `requests` directly.

```py
import requests

url = "https://books.toscrape.com/"
headers = {"User-Agent": "learning-python-scraper/1.0"}

response = requests.get(url, headers=headers, timeout=10)
response.raise_for_status()   # raises an error for 4xx / 5xx responses

print(response.status_code)   # 200 means success
```

```sh
200
```

Two small habits worth building:

- `timeout=10` stops your script hanging forever if the server does not answer.
- `raise_for_status()` fails loudly instead of letting you parse an error page by accident.

## Step 2: Parse it with BeautifulSoup

```py
import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
headers = {"User-Agent": "learning-python-scraper/1.0"}

response = requests.get(url, headers=headers, timeout=10)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.get_text(strip=True))
```

Use `response.text` (decoded text) when parsing, rather than `response.content` (raw bytes), unless you have a reason to handle encoding yourself.

Now find elements. The three methods you will use most:

```py
# first match only (returns None if nothing matches)
first_book = soup.find("article", class_="product_pod")

# all matches (returns a list, empty if nothing matches)
books = soup.find_all("article", class_="product_pod")

# CSS selectors, often the cleanest option
titles = soup.select("article.product_pod h3 a")
```

Extract data from each book:

```py
data = []
for book in books:
    title = book.h3.a["title"]               # attribute access
    price = book.select_one(".price_color").get_text(strip=True)
    link = book.h3.a["href"]
    data.append({"title": title, "price": price, "link": link})

print(data[:3])
```

Useful tools:

| Task | Code |
|---|---|
| Get text | `tag.get_text(strip=True)` |
| Get an attribute | `tag["href"]` or `tag.get("href")` |
| Filter by attribute | `soup.find_all("table", {"cellpadding": "3"})` |
| CSS selector | `soup.select("div.card > a")` |
| Safe lookup | `tag.get("href", "")` avoids a `KeyError` |

`{"cellpadding": "3"}` is an old HTML attribute used here as a filter. Newer pages normally use `class` or `id` instead.

## Step 3: Extract a table

Tables appear on many pages, Wikipedia especially. Here is how to read a table row by row:

```py
table = soup.find("table")
rows = table.find_all("tr")

header = [th.get_text(strip=True) for th in rows[0].find_all("th")]

records = []
for row in rows[1:]:
    cells = [td.get_text(strip=True) for td in row.find_all("td")]
    if cells:
        records.append(dict(zip(header, cells)))
```

**Shortcut with pandas.** If the table is in the raw HTML, one line does the job:

```py
import pandas as pd

tables = pd.read_html("https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States")
print(len(tables))
print(tables[0].head())
```

Install the extras first with `uv add pandas lxml`. Some sites reject the default pandas request, so you may need to download the page with `requests` (with a `User-Agent`) and pass `response.text` to `pd.read_html` using `io.StringIO`.

## Step 4: Save the data as JSON

```py
import json

with open("books.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
```

`encoding="utf-8"` and `ensure_ascii=False` keep special characters readable.

## The big modern problem: JavaScript-rendered pages

Try this on a page and you may find nothing in your results:

```py
soup.find_all("table")   # []
```

The reason is that `requests` only downloads the HTML the server sends. It does not run JavaScript. Many modern sites send a nearly empty page and then use JavaScript to load the data, so BeautifulSoup never sees it.

The UCI Machine Learning Repository is a good example. The old lesson used `https://archive.ics.uci.edu/ml/datasets.php` with `cellpadding="3"` tables. The site has since been redesigned (the list now lives at `https://archive.ics.uci.edu/datasets`) and is built with JavaScript, so that old code returns nothing.

### How to tell

1. Right-click the page in your browser and choose **View page source** (not Inspect). If the data you see on screen is missing from the source, JavaScript is loading it.
2. Or check in code: `print(len(soup.find_all("table")))` returns `0`.

### What to do about it, in order of preference

**1. Use an official package or API.** For UCI, the maintained package is `ucimlrepo`:

```sh
uv add ucimlrepo
```

```py
from ucimlrepo import fetch_ucirepo

iris = fetch_ucirepo(id=53)

print(iris.data.features.head())
print(iris.metadata)
```

**2. Find the hidden API the page calls.** Open the browser developer tools, go to the **Network** tab, filter by **Fetch/XHR**, then reload the page. You will often see a request that returns the data as JSON. Call it directly:

```py
import requests

api_url = "PASTE_THE_URL_YOU_FOUND_HERE"
data = requests.get(api_url, timeout=10).json()
```

No HTML parsing is needed, and it is faster and more stable than scraping.

**3. Drive a real browser with Playwright.** It runs the JavaScript for you:

```sh
uv add playwright
uv run playwright install
```

```py
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://archive.ics.uci.edu/datasets")
    page.wait_for_selector("h2")        # wait for content to appear
    html = page.content()
    browser.close()

soup = BeautifulSoup(html, "html.parser")
```

Notice that BeautifulSoup is still used at the end. Playwright gets the rendered page, and BeautifulSoup extracts from it.

## Choosing the right tool

| Situation | Tool |
|---|---|
| Static HTML page | `requests` + BeautifulSoup |
| Static HTML table | `pandas.read_html` |
| Data loaded by JavaScript, API visible | Call the API directly |
| Data loaded by JavaScript, no API | Playwright (or Selenium) |
| Crawling thousands of pages | Scrapy |
| Faster HTTP or async requests | `httpx` |
| Faster parsing | `lxml` or `selectolax` |
| Turning pages into clean text for LLMs | Firecrawl, Crawl4AI |

Start simple. Reach for a heavier tool only when the simpler one fails.

## Exercises: Day 22

1. Scrape [books.toscrape.com](https://books.toscrape.com) and store the title, price and rating of every book on the first page as a JSON file.
2. Extend exercise 1 to follow the "next" button and scrape all 50 pages. Add `time.sleep(1)` between requests and handle errors with `try/except`.
3. Scrape [quotes.toscrape.com](https://quotes.toscrape.com) and store each quote, its author and its tags as JSON.
4. Scrape the presidents table from [Wikipedia](https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States) and store it as JSON. The table is not very structured, so this takes patience. Do it once with BeautifulSoup and once with `pandas.read_html`, then compare.
5. Check the Boston University facts page (`https://www.bu.edu/president/boston-university-facts-stats/`). If it still serves plain HTML, scrape it and store the data as JSON. If the page has moved or changed, write down what you found and why it failed.
6. Get the list of UCI datasets and store it as JSON. First try `requests` and BeautifulSoup on `https://archive.ics.uci.edu/datasets` and confirm it returns no table. Then solve it using either the Network tab (find the API) or the `ucimlrepo` package.
7. Before scraping any site in this lesson, open its `robots.txt` and write down what it allows.

Bonus: choose a site you use yourself, work out whether it is static or JavaScript-rendered, and pick the right tool from the table above.

Congratulations! You are down to the last eight days.

[<< Day 21](../21_Day_Classes_and_objects/21_classes_and_objects.md) | [Day 23 >>](../23_Day_Virtual_environment/23_virtual_environment.md) API directly |
| Data loaded by JavaScript, no API | Playwright (or Selenium) |
| Crawling thousands of pages | Scrapy |
| Faster HTTP or async requests | `httpx` |
| Faster parsing | `lxml` or `selectolax` |
| Turning pages into clean text for LLMs | Firecrawl, Crawl4AI |

Start simple. Reach for a heavier tool only when the simpler one fails.

## Exercises: Day 22

1. Scrape [books.toscrape.com](https://books.toscrape.com) and store the title, price and rating of every book on the first page as a JSON file.
2. Extend exercise 1 to follow the "next" button and scrape all 50 pages. Add `time.sleep(1)` between requests and handle errors with `try/except`.
3. Scrape [quotes.toscrape.com](https://quotes.toscrape.com) and store each quote, its author and its tags as JSON.
4. Scrape the presidents table from [Wikipedia](https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States) and store it as JSON. The table is not very structured, so this takes patience. Do it once with BeautifulSoup and once with `pandas.read_html`, then compare.
5. Check the Boston University facts page (`https://www.bu.edu/president/boston-university-facts-stats/`). If it still serves plain HTML, scrape it and store the data as JSON. If the page has moved or changed, write down what you found and why it failed.
6. Get the list of UCI datasets and store it as JSON. First try `requests` and BeautifulSoup on `https://archive.ics.uci.edu/datasets` and confirm it returns no table. Then solve it using either the Network tab (find the API) or the `ucimlrepo` package.
7. Before scraping any site in this lesson, open its `robots.txt` and write down what it allows.

Bonus: choose a site you use yourself, work out whether it is static or JavaScript-rendered, and pick the right tool from the table above.

Congratulations! You are down to the last eight days.

[<< Day 21](../21_Day_Classes_and_objects/21_classes_and_objects.md) | [Day 23 >>](../23_Day_Virtual_environment/23_virtual_environment.md)